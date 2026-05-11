import time

import requests
import selectorlib
import smtplib, ssl
import os
import sqlite3

from cssselect.parser import Class

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, username, message)

        print("Email was sent!")


if __name__ == "__main__":
    while True:
        event = Event()
        scrapped = event.scrape(URL)
        extracted = event.extract(scrapped)

        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(database_path="data.db")
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                email = Email()
                email.send(message="Hey, new event was found")

        time.sleep(2)
