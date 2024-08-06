from datetime import datetime as dt

import pytest

from src.reminder import Reminder
from src.tests.reminder_cases import (
    AGE_VALUES,
    DATE_TIME_IN_FUTURE_VALUES,
    DAYS_TIL_VALUES,
    IS_ACTIVE_VALUES,
    TEST_LABELS,
)


def test_that_a_datetime_object_with_the_same_month_and_day_is_returned():
    input = {
        "name": "test",
        "year": 2000,
        "month": 1,
        "day": 1,
        "remind_in_days": [1],
        "emails": ["test@email.com"],
    }
    reminder = Reminder(**input)
    got = reminder.to_datetime()
    assert (
        got.month == 1 and got.day == 1
    ), f"Expected {dt(year=2000, month=1, day=1)} but got {got}"


@pytest.mark.parametrize(TEST_LABELS, DATE_TIME_IN_FUTURE_VALUES)
def test_that_a_datetime_object_with_a_future_year_is_returned(
    test_name, input, expected
):
    reminder = Reminder(**input)
    got = reminder.to_datetime()
    assert got.day == expected["day"]
    assert got.month == expected["month"]
    assert (
        got.year in expected["year"]
    ), f"{test_name} failed. Expected year {expected['year']} but got {got.year}"


@pytest.mark.parametrize(TEST_LABELS, DAYS_TIL_VALUES)
def test_that_days_til_is_calculated_correctly(test_name, input, expected):
    reminder = Reminder(**input)
    got = reminder.days_til()
    assert got == expected, f"{test_name} failed. Expected {expected} but got {got}"


@pytest.mark.parametrize(TEST_LABELS, IS_ACTIVE_VALUES)
def test_that_is_active_is_calculated_correctly(test_name, input, expected):
    reminder = Reminder(**input)
    got = reminder.is_active()
    assert got == expected, f"{test_name} failed. Expected {expected} but got {got}"


@pytest.mark.parametrize(TEST_LABELS, AGE_VALUES)
def test_that_age_is_calculated_correctly(test_name, input, expected):
    reminder = Reminder(**input)
    got = reminder.age()
    assert got == expected, f"{test_name} failed. Expected {expected} but got {got}"
