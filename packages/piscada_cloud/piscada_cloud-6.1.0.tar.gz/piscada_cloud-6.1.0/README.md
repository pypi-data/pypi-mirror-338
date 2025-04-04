# Picada Cloud

Library for the Piscada Cloud including authentication and data access.

## Features

- Login to Piscada Cloud and retrieve credentials
- Persist credentialss locally
- Read historic values for multiple tags as a Pandas DataFrame
- Possible apply time-based linear interpolation to measurements
- Utils to add fractional representations of periods: day, week, year

## Install

Install from PyPI:

```shell
pip install piscada-cloud
```

or

```shell
poetry add piscada-cloud
```

Install from local source:

```shell
pip install --editable path/to/piscada_cloud
```

or

```shell
poetry add path/to/piscada_cloud
```

## Usage

### Authentication

To log-in interactively and persist the retrieved credentials on disk (under `$HOME/.piscada_credentials`) simply run:

```shell
python -m piscada_cloud.auth
```

or

```shell
poetry run python -m piscada_cloud.auth
```

Any future invocation, e.g. `credentials = piscada_cloud.auth.persisted_login()` will return the credentials on disk without user interaction.

`credentials = piscada_cloud.auth.login(username, password, host)` can be used to retrieve the credentials programmatically.

### Getting Data

The credentials retrieved through the login can be used to get the host and acccesss-token for the historical data API:

```python
from piscada_cloud import auth

credentials = auth.login_persisted()
host, token = auth.get_historian_credentials(credentials)
```

The host and token can be used to retrieve historic data as a Pandas DataFrame.
The `get_historic_values` method takes a row of parameters:

- controller: e.g. `0798ac4a-4d4f-4648-95f0-12676b3411d5`
- start date as ISO8601 string: e.g. `2019-08-01T00:00Z`
- end date as ISO8601 string: e.g. `2019-08-01T00:00Z`
- a list of tags: e.g. `["oBU136003RT90_MV|linear", "oBU136003QD40_A1"]` which can optionally include the suffix `|linear` to enable linear time-based interpolation on this tag.
- Endpoint to which we send the historian queries. e.g. `historian.piscada.online`. Optional.
- Access token, associated with the endpoint, used for authentication. Optional.

```python
from piscada_cloud.data import get_historic_values

data = get_historic_values(
    "0798ac4a-4d4f-4648-95f0-12676b3411d5",
    "2019-08-01T00:00Z",
    "2019-08-31T23:59Z",
    [
        "oBU136003RT90_MV|linear",
        "oBU136003QD40_A1",
    ],
)
```

## Write Data

In this example the column `oCU135001RT90_MV` is selected and the average value is calculated using the method `.mean()`.

To write the result back to the Piscada Cloud, the `data` module offers the `write_value` function. It takes three arguments: `controller_id`, `target_tag`, and `value`.

The `target_tag` must use the prefix `py_` as this is the only namespace allowed for writing data via the API.

```python
mean = data_frame["oCU135001RT90_MV"].mean()
print(mean)
response = write_value("0798ac4a-4d4f-4648-95f0-12676b3411d5", "py_oCU135001RT90_MV_1h_mean", mean)
if response.ok:
    print("OK")
else:
    print(response.text)
```

The `response` returned by the `write_value` method allows to check if the writing of data was successful `response.ok == True`.

### Manipulations

In order to support analysis in the context of periodic patters, the `manipulations` allow you to add fractional representations of day, week, and year as additional columns in the DataFrame:

- 00:00:00 -> 0.0 --- 23:59:59 -> 1.0
- Monday 00:00:00 -> 0.0 --- Sunday 23:59:59 -> 1.0
- 1st Jan. 00:00:00 -> 0.0 --- 31st Dec. 23:59:59 -> 1.0

```python
from piscada_cloud import manipulations

manipulations.add_weekdays(data)
manipulations.add_day_fraction(data)
manipulations.add_week_fraction(data)
manipulations.add_year_fraction(data)
```

## Development

Enable the provided git pre commit hook: `ln -s ./qa.sh .git/hooks/pre-commit`

## Requirements

The package will support the two latest version of Python.

## Authors

- Tim Jagenberg [tim.jagenberg@piscada.com](mailto:tim.jagenberg@piscada.com)
- Filip Henrik Larsen [filip.larsen@piscada.com](mailto:filip.larsen@piscada.com)

## License

© Piscada AS 2019
