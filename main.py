import time

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
