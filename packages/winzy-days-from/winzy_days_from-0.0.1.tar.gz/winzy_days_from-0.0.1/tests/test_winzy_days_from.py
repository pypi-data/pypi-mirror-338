import pytest
from datetime import datetime, timedelta
import winzy_days_from as w

from argparse import Namespace, ArgumentParser


def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(["10"])
    assert result.days == 10
    assert result.date is None


def test_plugin(capsys):
    w.daysfrom_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``winzy`` plugin." in captured.out


def test_calculate_future_date_with_given_date():
    start_date = "2023-01-01"
    days = 10
    expected_date = (
        datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=days)
    ).strftime("%Y-%m-%d")
    assert w.calculate_future_date(start_date, days) == expected_date


def test_calculate_future_date_with_today_date():
    days = 5
    today = datetime.now()
    expected_date = (today + timedelta(days=days)).strftime("%Y-%m-%d")
    assert w.calculate_future_date(None, days) == expected_date


def test_calculate_future_date_with_negative_days():
    start_date = "2023-01-01"
    days = -10
    expected_date = (
        datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=days)
    ).strftime("%Y-%m-%d")
    assert w.calculate_future_date(start_date, days) == expected_date


def test_calculate_future_date_with_invalid_date():
    with pytest.raises(ValueError):
        w.calculate_future_date("invalid-date", 10)
