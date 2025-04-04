"""Template classes for cloud functions.

This module has a collection of Cloud function template classes that can be practical to inherit from.
An example usage is shown at the bottom of the file, and is used when running the file.

This module holds these classes:
    * CloudFunctionTemplate
"""
from datetime import datetime, timedelta
from typing import Dict, Union

from pandas import DataFrame

from piscada_cloud.data import get_historic_values, write_value
from piscada_cloud.manipulations import count_errors
from piscada_cloud.mappings import MappingTable, Tag
from piscada_cloud.results import Result, Value, write_result


def check_tag_name_in_list(tag, tag_names):
    """Check if a tag's name is listen in a list of tag names."""
    if isinstance(tag, Tag):
        if tag.name in tag_names:
            return True
    elif isinstance(tag, list):
        for tag_list_item in tag:
            if tag_list_item.name in tag_names:
                return True
    else:
        raise RuntimeError(
            f"ERROR: Misconfigured Tags. All values in `self.tags` and `self.status_tags` should be of type Tag or List[Tag]. Got {tag} of type {type(tag)}."
        )
    return False


class CloudFunctionTemplate:
    """
    Template class holding most common steps for most cloud functions.

    This class works as a skeleton for other classes to inherit from and expand.
    Some of the methods are required, and will raise an `NotImplemetedError` if not overridden in the subclass.

    Methods required to be overridden:
        - `set_tags()`
        - `set_status_tags()`
        - `set_initial_result()`

    While all other methods are optional, some will need to be overridden in order to make any sense, e.g. `calculate_derived_columns()`.
    `self.status_tags` is assumed to have the keys "ERROR", "ERROR_1D", "ERROR_7D", "ERROR_30D" and "ERROR_JSON".
    Their values are the tags to which we write status updates, daily-, weekly-, and monthly aggregated results, and a json result object, respectively.
    If other key names are to be used, these can be passed as arguments to the relevant methods.
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, mapping_table: MappingTable, now: datetime):
        """
        Set up and check input arguments.

        Save input arguments as properties in addition to setting up placeholders for expected values.

        Parameters
        ----------
        mapping_table : MappingTable
            Mapping table for which we evaluate the status.
        now : datetime
            Timestamp of evaluation.
        """
        self.mapping_table = mapping_table
        self.tags = self.set_tags()
        self.status_tags = self.set_status_tags()
        self.check_missing_tags()
        self.now = now
        self.last_state = 0
        self.last_run: datetime
        self.last_error_start: datetime
        self.data_frame: DataFrame
        self.result: Result = self.set_initial_result()

    def set_tags(self) -> Dict[str, Tag]:
        """
        Construct a dictionary of tags that data will be fetched from.

        Returns
        -------
        dict
            A dictionary whose values are tags or list of tags.

        Raises
        ------
        NotImplementedError
            If a subclass does not override this method.
        """
        raise NotImplementedError("When subclassing from CloudFunctionTemplate, you must override the `set_tags()` method.")

    def set_status_tags(self) -> Dict[str, Tag]:
        """
        Construct a dictionary of service tags that results shall be written to.

        Idealy

        Returns
        -------
            A dictionary whose values are tags or list of tags.

        Raises
        ------
        NotImplementedError
            If a subclass does not override this method.
        """
        raise NotImplementedError("When subclassing from CloudFunctionTemplate, you must override the `set_status_tags()` method.")

    def set_initial_result(self) -> Result:
        """
        Construct an initial value for the result object.

        Returns
        -------
        Result
            A result object with fully specified observation, ratings and observed_values_type, and observed_values as an empty list.

        Raises
        ------
        NotImplementedError
            If a subclass does not override this method.
        """
        raise NotImplementedError("When subclassing from CloudFunctionTemplate, you must override the `set_result()` method.")

    def check_missing_tags(self):
        """
        Check if any values in self.tags or self.status_tags is None.

        First check if any value in the dictionary is `None`, since `get_tag()` returns `None` for missing tags.
        Then check if the tag is in the mapping_tables tag mapping.

        Raises
        ------
        RuntimeError
            If any tag mapping in `self.tags` or `self.status_tags` does not hold a Tag object or a list of Tag objects.
        """
        missing_tags = [str(key) for key, value in self.tags.items() if value is None]
        missing_tags.extend([str(key) for key, value in self.status_tags.items() if value is None])
        if missing_tags:
            raise RuntimeError("ERROR: Missing Tags: " + ", ".join(missing_tags))

        tag_mapping_tags = [tag_mapping.tag for tag_mapping in self.mapping_table.tag_mappings]
        missing_tags = [str(key) for key, tag in self.tags.items() if not check_tag_name_in_list(tag, tag_mapping_tags)]
        missing_tags.extend([str(key) for key, tag in self.status_tags.items() if not check_tag_name_in_list(tag, tag_mapping_tags)])
        if missing_tags:
            raise RuntimeError("ERROR: Missing Tags: " + ", ".join(missing_tags))

    def update_last_run(self, error_tag: str = "ERROR", initial_window: timedelta = timedelta(minutes=30)) -> Union[Dict[str, str], str]:
        """
        Fetch the last error entry from the `error_tag` and update `self.last_run` and `self.last_state` accordingly.

        If there are no previous entries, set `self.last_run` to be `initial_window` before `self.now`.

        Parameters
        ----------
        error_tag : str
            Key in `self.status_tags` holding the tag to fetch error states from. Defaults to "ERROR".
        initial_window : timedelta
            Time span to look back in time for the initial run. Defaults to 30 minutes.

        Returns
        -------
        Union[Dict[str, str], str]
            Status report for logging. One line for every attribute set.
        """
        log = {}
        status_tag = self.status_tags[error_tag]
        df_status = get_historic_values(self.now, self.now, [status_tag])
        if df_status is not None and not df_status.empty:
            self.last_run = df_status.index.max().to_pydatetime()
            self.last_state = int(df_status.iloc[-1][str(status_tag)])
            log["last_run"] = str(self.last_run)
            log["last_state"] = str(self.last_state)
            if self.last_state:
                self.last_error_start = self.last_run
            else:
                df_err = get_historic_values(self.last_run - timedelta(milliseconds=1), self.last_run - timedelta(milliseconds=1), [status_tag])
                if df_err is not None and not df_err.empty:
                    self.last_error_start = df_err.index.max().to_pydatetime()
            log["last_error_start"] = str(self.last_error_start) if hasattr(self, "last_error_start") else "Not set."
            return log

        # If we have never run before, look back `initial_window` from now.
        self.last_run = self.now - initial_window
        self.last_error_start = self.last_run
        return f"No last run found. Set last run and last error start to {self.last_run}."

    def update_data(self, additional_timedelta: timedelta = timedelta(0), max_time_range: timedelta = timedelta(hours=2)) -> str:
        """
        Fetch data for the tags in `self.tags` and store the resulting dataframe in `self.data_frame`.

        By default data will be fetched from the time of the last run until now.
        The parameter `additional_timedelta` can be set to change the starting point of this query.

        Parameters
        ----------
        additional_timedelta : timedelta
            Move the stating point for the query.

        Returns
        -------
        str
            Status report for logging.
        """
        time_range_adjustment_warning = ""
        start = self.last_run - additional_timedelta
        if self.now - start > max_time_range:
            start = self.now - max_time_range
            time_range_adjustment_warning = f"Last run is too long ago. Adjusting `start` to fit `max_time_range` ({max_time_range})."
        self.data_frame = get_historic_values(start, self.now, list(self.tags.values()))
        if self.data_frame is not None and not self.data_frame.empty:
            return (
                time_range_adjustment_warning
                + f"Retrieved {len(self.data_frame)} rows of data in the period {self.data_frame.index.min()} to {self.data_frame.index.max()}."
            )
        return time_range_adjustment_warning + f"ERROR: Could not retrieved data for the period {start} to {self.now}."

    def calculate_derived_columns(self) -> str:
        """
        Calculate derived values and add them as columns to `self.data_frame`.

        Returns
        -------
        str
            Status report for logging.
        """
        raise NotImplementedError(
            f"calculate_derived_columns() was not implemented in {self.__class__.__name__}. This method is optional. If you don't need it, don't use it."
        )

    def calculate_status(self) -> str:
        """
        Calculate status from values in `self.data_frame` and add it as a column.

        Returns
        -------
        str
            Status report for logging.
        """
        raise NotImplementedError("When subclassing from CloudFunction, you must override the `calculate_status()` method.")

    def send_status_changes(self, error_tag: str = "ERROR", status_column: str = "status") -> Union[Dict[str, str], str]:
        """
        Send status changes since last run.

        If there are no changes since the last run, send the same value as from the last run.

        Parameters
        ----------
        error_tag : str
            Key in `self.status_tags` holding the tag to fetch error states from. Defaults to "Error".
        status_column : str
            Name of column holding the status in `self.data_frame`. Defaults to "status".

        Raises
        ------
        RuntimeError
            If post requests are denied by the server.

        Returns
        -------
        Union[Dict[str, str], str]
            Status report for logging. One line for every state change written to database.
        """
        log = {}
        new = self.data_frame.loc[self.data_frame.index > self.last_run, status_column]
        status_changes = new != new.shift(1)
        if not status_changes.empty:
            status_changes[0] = new[0] != self.last_state
            updates = new[status_changes]
            if not updates.empty:
                for timestamp, state in updates.iteritems():
                    response = write_value(self.status_tags[error_tag], state, int(timestamp.timestamp() * 1000))
                    if response.status_code < 200 or response.status_code >= 300:
                        raise RuntimeError(f"Could not send state change {timestamp}: {str(self.status_tags[error_tag])} - {state}. Reason: {response.reason}")
                    if state:
                        self.last_error_start = timestamp.to_pydatetime()
                    log[str(timestamp)] = f"Sent status change: {state} to tag {str(self.status_tags[error_tag])}"
                self.result.observed_values.append(
                    Value(
                        name="Last observed state",
                        type="",
                        unit="",
                        value=int(state),  # pylint: disable=undefined-loop-variable
                        timestamp=timestamp.isoformat(),  # pylint: disable=undefined-loop-variable
                    )
                )

                return log
        response = write_value(self.status_tags[error_tag], self.last_state, int(self.last_run.timestamp() * 1000))
        if response.status_code < 200 or response.status_code >= 300:
            raise RuntimeError(
                f"No status changes. Could not send last state {self.last_run}: {str(self.status_tags[error_tag])} - {self.last_state}. Reason: {response.reason}"
            )
        self.result.observed_values.append(Value(name="Last observed state", type="", unit="", value=int(self.last_state), timestamp=self.last_run.isoformat()))
        return f"No status changes. Sent last calculated state: {self.last_run}: {str(self.status_tags[error_tag])} - {self.last_state}"

    def sum_up_past_states(
        self, error_tag: str = "ERROR", error_1d_tag: str = "ERROR_1D", error_7d_tag: str = "ERROR_7D", error_30d_tag: str = "ERROR_30D"
    ) -> Dict[int, str]:
        """
        Compute sum of errors the past day, week and month.

        Query the historian for error statuses the past month and aggregate the number of errors for slices of this dataset.
        By default the aggregation is a count.

        Parameters
        ----------
        error_tag : str
            Key in `self.status_tags` corresponding to the error status tag. Defaults to "ERROR"
        error_1d_tag : str
            Key in `self.status_tags` corresponding to the tag for 1 day error aggregate. Defaults to "ERROR_1D"
        error_7d_tag : str
            Key in `self.status_tags` corresponding to the tag for 7 days error aggregate. Defaults to "ERROR_7D"
        error_30d_tag : str
            Key in `self.status_tags` corresponding to the tag for 30 days error aggregate. Defaults to "ERROR_30D"

        Raises
        ------
        RuntimeError
            If post requests are denied by the server.

        Returns
        -------
        Dict[str, str]
            Status report for logging. One entry for every aggregate.
        """
        # pylint: disable-msg=too-many-locals
        status_tag = self.status_tags[error_tag]
        write_tags = {1: self.status_tags[error_1d_tag], 7: self.status_tags[error_7d_tag], 30: self.status_tags[error_30d_tag]}
        end = self.now
        start = end - timedelta(days=30)
        status_df = get_historic_values(start, end, [status_tag])
        log = {}
        for days in write_tags:
            start = end - timedelta(days=days)
            window_df = status_df.loc[start:end]  # type: ignore
            if window_df.empty:
                self.result.observed_values.append(Value(name=f"Last {days} days", type="", unit="", value=""))
                log[days] = f"No data found for given time range {start} - {end}. Sent {days}-days error sum: {write_tags[days]} - {None}."
                continue
            count = count_errors(window_df, column=str(status_tag))
            timestamp = window_df.index.max()
            response = write_value(write_tags[days], value=count, timestamp=int(timestamp.timestamp() * 1000))
            if response.status_code < 200 or response.status_code >= 300:
                raise RuntimeError(f"Could not send {days}-days error sum: {timestamp}: {write_tags[days]} - {count}. Reason: {response.reason}")
            self.result.observed_values.append(Value(name=f"Last {days} days", type="", unit="", value=count, timestamp=timestamp.isoformat()))
            log[days] = f"Sent {days}-days error sum: {timestamp}: {write_tags[days]} - {count}."
        return log

    def write_result(self, error_json_tag: str = "ERROR_JSON", allow_empty_results=False):
        """
        Write the result object as json to the database.

        Parameters
        ----------
        error_json_tag : str
            Key in `self.status_tags` corresponding to the tag error status json objects. Defaults to "ERROR_JSON".

        Raises
        ------
        RuntimeError
            If post request is denied by the server.

        Returns
        -------
        str
            Status report for logging.
        """
        error_sum = sum([observed_value.value for observed_value in self.result.observed_values if isinstance(observed_value.value, (int, float, bool))])
        if error_sum == 0 and not allow_empty_results:
            return "No errors detected the past 30 days. Not sending result."
        response = write_result(tag=self.status_tags[error_json_tag], result=self.result, timestamp=int(self.last_error_start.timestamp() * 1000))
        if response.status_code < 200 or response.status_code >= 300:
            raise RuntimeError(f"Could not send result! Reason: {response.reason}")
        return f"Sent results to {self.status_tags[error_json_tag]}."
