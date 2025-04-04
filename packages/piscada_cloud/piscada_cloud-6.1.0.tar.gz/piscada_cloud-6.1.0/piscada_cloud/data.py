"""Data module containing functions which enables reading/writing data from/to the Piscada Cloud."""
import json
import logging
import os
import time
from datetime import datetime
from typing import Dict, List, Union

import pandas
import requests
from pandas import DataFrame
from requests import Response

from piscada_cloud.mappings import Tag


def get_historic_values(  # pylint: disable=R0914
    start: datetime, end: datetime, tags: List[Tag], host: Union[str, None] = None, token: Union[str, None] = None
) -> DataFrame:
    """Retrieve historic values for a controller and a list of tags between the given dates as a Pandas DataFrame.

    Parameters
    ----------
    start : datetime
        The start of the window, including the last valid value in the database before this moment.
    end : datetime
        The end of the window, including the last valid value in the database before this moment.
    tag: List[Tag]
        The list of tags (controller-tag combinations) for which to request data.
    host: str, optional
        Endpoint to send get request. Overrides the default, which is os.environ['HISTORIAN_HOST'].
    token: str, optional
        Access token accosiated with the host. Overrides the default, which is os.environ['HISTORIAN_TOKEN'].

    Returns
    -------
    DataFrame
        The queried data in for of a Pandas DataFrame as a time-series. Index is 'timestamp', columns are named 'CONTROLLER_ID|TAG'.

    Raises
    ------
    RuntimeError
        If not data could be retrieved.
    """
    if not host:
        host = os.getenv("HISTORIAN_HOST")
    if not token:
        token = os.getenv("HISTORIAN_TOKEN")
    if not (host and token):
        raise RuntimeError(
            """
            Historian host and token need to be defined.
            These can be passed as arguments to get_historic_values() or set
            as environment variables 'HISTORIAN_HOST' and 'HISTORIAN_TOKEN'
            """
        )

    header: Dict[str, str] = {"Authorization": "Bearer " + token}  # pylint: disable=R0914
    data_frames: List[DataFrame] = []
    start_s = start.isoformat(sep="T", timespec="milliseconds").replace("+", "%2B")
    end_s = end.isoformat(sep="T", timespec="milliseconds").replace("+", "%2B")
    for tag in set(tags):
        logging.debug("Downloading data for tag '%s'...", tag)
        response_value = requests.get(f"https://{host}/{tag.controller_id}/value/{tag.name}?ts={start_s}&time_format=epoch", headers=header)
        response_series = requests.get(f"https://{host}/{tag.controller_id}/timeseries/{tag.name}?from={start_s}&to={end_s}&time_format=epoch", headers=header)
        logging.debug("Finished downloading data for tag '%s'.", tag)
        logging.debug("Converting data for tag '%s' to Pandas DataFrame...", tag)
        if response_value.status_code == 200:
            value_dict = response_value.json()
            data_frame_value = pandas.DataFrame([[value_dict["ts"], float(value_dict["value"])]], columns=["ts", "v"])
        else:
            data_frame_value = DataFrame()
        if response_series.status_code == 200:
            data_frame_series = pandas.read_json(response_series.text, orient="records", convert_dates=False)
        else:
            data_frame_series = DataFrame()
        data_frame = pandas.concat([data_frame_value, data_frame_series], sort=False)
        data_frame.drop_duplicates(inplace=True)
        if not data_frame.empty:
            data_frame["timestamp"] = pandas.to_datetime(data_frame["ts"], unit="ms", utc=True)
            data_frame.set_index("timestamp", inplace=True)
            data_frame.drop(["ts"], axis=1, inplace=True)
            data_frame.rename(columns={"v": str(tag)}, errors="raise", inplace=True)
            logging.debug("Finished converting data for tag '%s' to Pandas DataFrame.", tag)
        else:
            logging.warning("Could not load any data for tag %s start %s end %s", tag, start_s, end_s)
        data_frames.append(data_frame)
    logging.debug("Joining tags into single Pandas DataFrame...")
    if len(data_frames) > 0:
        result: DataFrame = data_frames[0].join(data_frames[1:], how="outer")
        result.sort_index(inplace=True)
        logging.debug("Finished joining tags into single Pandas DataFrame.")
        result.ffill(inplace=True)
        result.dropna(inplace=True)
        return result
    raise RuntimeError(f"Could not load any of the requested data: {tags} {start_s} {end_s}")


def write_value(
    tag: Tag, value: Union[int, float, dict, str], timestamp: int = int(time.time() * 1000), host: Union[str, None] = None, token: Union[str, None] = None
) -> Response:
    """
    Write the given value to the given tag (combination of controller/tag).

    Parameters
    ----------
    tag : Tag
        The controller-tag combination to write the value to.
    value : Union[int, float, dict, str]
        The float, string, or dict value to write to the controller-tag combination. Float and string will be sent as is, dict will be serialised as JSON string.
    timestamp: int, optional
        The timestamp in milliseconds since epoch at which to write the value, by default int(time.time() * 1000).
    host: str, optional
        Endpoint to send post request. Overrides the default, which is os.environ['WRITEAPI_HOST'].
    token: str, optional
        Access token accosiated with the host. Overrides the default, which is os.environ['WRITEAPI_TOKEN'].

    Returns
    -------
    Response
        The response of the api for the write request.
    """
    if not host:
        host = os.getenv("WRITEAPI_HOST")
    if not token:
        token = os.getenv("WRITEAPI_TOKEN")
    if not (host and token):
        raise RuntimeError(
            """
            Writeapi host and token need to be defined. These can be passed
            as arguments to write_values() or set as environment
            variables 'WRITEAPI_HOST' and 'WRITEAPI_TOKEN'
            """
        )
    url = f"https://{host}/v1/controllers/{tag.controller_id}/tags/{tag.name}"
    if isinstance(value, (int, float)):
        payload = {
            "timestamp": timestamp,
            "dataType": "number",
            "value": value,
        }
    elif isinstance(value, str):
        payload = {
            "timestamp": timestamp,
            "dataType": "string",
            "valueText": value,
        }
    elif isinstance(value, dict):
        value = json.dumps(value)
        payload = {
            "timestamp": timestamp,
            "dataType": "string",
            "valueText": value,
        }
    else:
        raise TypeError(f"Incompatible data provided: {type(value)}")
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + token,
    }
    logging.debug("Writing value %s to %s", json.dumps(payload), url)
    response = requests.post(url, json=payload, headers=headers)
    return response
