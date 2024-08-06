from datetime import datetime as dt

today = dt.today()


TEST_LABELS = ["test_name", "input", "expected"]

DATE_TIME_IN_FUTURE_VALUES = [
    (
        "a datetime object with a future year is returned when year is 2000",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 1,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
        },
        {"month": 1, "day": 1, "year": [today.year, today.year + 1]},
    ),
    (
        "a datetime object with this year is returned when year is None and month and day is today",
        {
            "name": "test",
            "year": None,
            "month": today.month,
            "day": today.day,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
        },
        {
            "month": today.month,
            "day": today.day,
            "year": [today.year],
        },
    ),
]

DAYS_TIL_VALUES = [
    (
        "days til is calculated correctly for a week in the future",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 7,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=1),
        },
        6,
    ),
    (
        "days til is calculated correctly for today",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 7,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=7),
        },
        0,
    ),
    (
        "days til is calculated correctly for a year in the future on a leap year",
        {
            "name": "test",
            "year": 2001,
            "month": 1,
            "day": 7,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=7),
        },
        366,
    ),
    (
        "days til is calculated correctly for a year in the future on a regular year",
        {
            "name": "test",
            "year": 2002,
            "month": 1,
            "day": 7,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
            "today": dt(year=2001, month=1, day=7),
        },
        365,
    ),
]

IS_ACTIVE_VALUES = [
    (
        "is active is shown correctly for today",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 7,
            "remind_in_days": [1, 0],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=7),
        },
        True,
    ),
    (
        "is active is not shown for day when 0 is not in remind_in_days",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 7,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=7),
        },
        False,
    ),
    (
        "is active is shown correctly for tomorrow",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 7,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=6),
        },
        True,
    ),
    (
        "is active is not shown for tomorrow when only 0 is in remind_in_days",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 7,
            "remind_in_days": [0],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=6),
        },
        False,
    ),
    (
        "is active is shown for a reminder in 1 week",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 14,
            "remind_in_days": [7],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=7),
        },
        True,
    ),
    (
        "is active is shown for a reminder in 3 days",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 14,
            "remind_in_days": [3],
            "emails": ["test@email.com"],
            "today": dt(year=2000, month=1, day=11),
        },
        True,
    ),
]

AGE_VALUES = [
    (
        "age is calculated correctly for a year ago",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 1,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
            "today": dt(year=2001, month=1, day=1),
        },
        1,
    ),
    (
        "age is calculated correctly for 21 years ago",
        {
            "name": "test",
            "year": 2000,
            "month": 1,
            "day": 1,
            "remind_in_days": [1],
            "emails": ["test@email.com"],
            "today": dt(year=2021, month=1, day=1),
        },
        21,
    ),
]
