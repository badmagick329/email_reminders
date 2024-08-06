from config import Config
from reminder import Reminder

config = Config()


def read_reminders():
    return [
        {
            "name": "test",
            "year": None,
            "month": 8,
            "day": 6,
            "remind_in_days": [1, 0],
            "emails": [config.test_address],
        }
    ]


def main():
    reminders = read_reminders()
    for reminder_args in reminders:
        reminder = Reminder(**reminder_args)
        print(reminder)
        print(reminder.is_active())
        print(reminder.days_til())


if __name__ == "__main__":
    main()
