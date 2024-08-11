import json
import logging

from config import Config
from consts import REMINDERS_FILE
from reminder import Reminder
from sender import SMTPSender

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="reminder_logs.log",
    filemode="a",
)

config = Config()


def main():
    reminders = read_reminders()
    sender = SMTPSender(config)
    logging.info(f"Script started. {len(reminders)} reminders found")

    for reminder_args in reminders:
        reminder = Reminder(**reminder_args)
        if not reminder.is_active():
            continue

        send_emails(sender, reminder)


def read_reminders():
    with open(REMINDERS_FILE, "r", encoding="utf-8") as f:
        reminders_list = json.load(f)
    return reminders_list


def send_emails(sender: SMTPSender, reminder: Reminder):
    for name in reminder.emails:
        address = config.resolve_address(name)
        if not address:
            continue

        logging.info(f"Sending email to {address} about {reminder.name}")
        subject = get_subject(reminder)
        content = get_content(reminder)
        err = sender.send_mail(address, subject, content)
        if err is not None:
            logging.info(f"Failed to send email to {address}: {err}")


def get_subject(reminder: Reminder):
    days_til = reminder.days_til()
    days_text = "today" if days_til == 0 else f"in {days_til} days"
    return f"Reminder {days_text}"


def get_content(reminder: Reminder):
    content = f"Reminder: {reminder.name}"
    date_text = f"{reminder.month}-{reminder.day}"
    if reminder.year:
        date_text = f"{reminder.year}-{date_text}"
    content = f"Reminder: {reminder.name} ({date_text})"

    age = reminder.is_birthday() and reminder.age()
    if age is not False:
        content += f"\nThey will be {age} years old"
    return content


if __name__ == "__main__":
    # _test()
    main()
