import smtplib
from datetime import datetime as dt

from config import Config


class SMTPSender:

    def __init__(self):
        self.config = Config()
        print(f"Config file: {self.config.config_file}")
        self.server = smtplib.SMTP_SSL(self.config.smtp_host, 465)
        self.server.login(self.config.smtp_user, self.config.smtp_password)

    def send_mail(self, to, subject, content) -> Exception | None:
        try:
            print("Sending email at", dt.now())
            msg = f"Subject: {subject}\n\n{content}"
            self.server.sendmail(self.config.smtp_user, to, msg)
            print("sent")
        except Exception as e:
            return e

    def test_send(self) -> Exception | None:
        self.send_mail(self.config.test_address, "test email", "test content")


def main():
    sender = SMTPSender()
    sender.test_send()


if __name__ == "__main__":
    main()
