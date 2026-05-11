import smtplib
import ssl
import os


class EmailSender:
    """Handles sending email notifications for new events"""

    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = 465
        self.username = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")

    def send(self, message: str) -> None:
        """Sends an email alert with the given message"""

        context = ssl.create_default_context()

        # Proper email format requires a Subject line
        formatted_message = f"Subject: New Tour Event Found!\n\n{message}"

        with smtplib.SMTP_SSL(self.host, self.port, context=context) as server:
            server.login(self.username, self.password)
            server.sendmail(self.username, self.username, formatted_message)

        print("Email notification sent successfully!")
