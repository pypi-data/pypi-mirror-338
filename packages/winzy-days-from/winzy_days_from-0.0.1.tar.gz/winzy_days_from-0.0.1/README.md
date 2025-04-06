# winzy-days-from

[![PyPI](https://img.shields.io/pypi/v/winzy-days-from.svg)](https://pypi.org/project/winzy-days-from/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/winzy-days-from?include_prereleases&label=changelog)](https://github.com/sukhbinder/winzy-days-from/releases)
[![Tests](https://github.com/sukhbinder/winzy-days-from/workflows/Test/badge.svg)](https://github.com/sukhbinder/winzy-days-from/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/winzy-days-from/blob/main/LICENSE)

Calculates future date from number of days

## Installation

First [install winzy](https://github.com/sukhbinder/winzy) by typing

```bash
pip install winzy
```

Then install this plugin in the same environment as your winzy application.
```bash
winzy install winzy-days-from
```
## Usage

To get help type ``winzy  daysfrom --help``

```bash
usage: winzy daysfrom [-h] [--date DATE] days

Calculate a future date based on a given date and number of days.

positional arguments:
  days         Number of days to add to the date.

optional arguments:
  -h, --help   show this help message and exit
  --date DATE  Start date in yyyy-mm-dd format (default: today).

```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd winzy-days-from
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
