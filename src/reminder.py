from datetime import datetime as dt
from datetime import timedelta

from pydantic import BaseModel, field_validator


class Reminder(BaseModel):
    name: str
    month: int
    day: int
    remind_in_days: list[int]
    emails: list[str]
    year: int | None = None
    today: dt | None = None
    recurring: bool = True

    @field_validator("remind_in_days")
    def check_remind_in_days(cls, v):
        assert all(
            isinstance(i, int) for i in v
        ), "remind_in_days must be a list of integers"

        assert all(
            i >= 0 for i in v
        ), "remind_in_days must be a list of positive integers"
        return v

    @field_validator("year")
    def check_year(cls, v):
        assert v is None or isinstance(v, int), "year must be an integer or None"
        return v

    @field_validator("month")
    def check_month(cls, v):
        assert isinstance(v, int), "month must be an integer"
        assert 1 <= v <= 12, "month must be between 1 and 12"
        return v

    @field_validator("day")
    def check_day(cls, v):
        assert isinstance(v, int), "day must be an integer"
        assert 1 <= v <= 31, "day must be between 1 and 31"
        return v

    @field_validator("name")
    def check_name(cls, v):
        assert isinstance(v, str), "name must be a string"
        assert len(v) > 0, "name must not be empty"
        return v

    @field_validator("emails")
    def check_emails(cls, v):
        assert all(isinstance(i, str) for i in v), "emails must be a list of strings"
        return v

    def to_datetime(self) -> dt:
        year = self.datetime_today.year if self.year is None else self.year
        datetime_for_reminder = dt(year=year, month=self.month, day=self.day)
        if not self.recurring:
            return datetime_for_reminder

        while self.datetime_today - datetime_for_reminder > timedelta(0):
            year += 1
            datetime_for_reminder = dt(year=year, month=self.month, day=self.day)

        assert self.datetime_today - datetime_for_reminder <= timedelta(
            0
        ), "datetime_for_reminder must be in the future for a recurring reminder"
        return datetime_for_reminder

    @property
    def datetime_today(self):
        if self.today is None:
            self.today = dt.today()
        if (
            self.today.hour != 0
            or self.today.minute != 0
            or self.today.second != 0
            or self.today.microsecond != 0
        ):
            self.today = self.today.replace(hour=0, minute=0, second=0, microsecond=0)
        return self.today

    def days_til(self) -> int:
        return (self.to_datetime() - self.datetime_today).days

    def is_active(self) -> bool:
        return self.days_til() in self.remind_in_days

    def is_birthday(self) -> bool:
        return "birthday" not in self.name.lower()

    def age(self) -> int | None:
        if self.year is None:
            return None

        return self.datetime_today.year - self.year
