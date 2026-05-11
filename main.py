import time

from modules import Event, Database, EmailSender

if __name__ == "__main__":
    # Initialize objects outside the loop to prevent unnecessary memory allocation
    event_manager = Event()
    db_manager = Database()
    email_manager = EmailSender()

    while True:
        scraped_data = event_manager.scrape()
        extracted_data = event_manager.extract(scraped_data)

        print(f"Current website status: {extracted_data}")

        if extracted_data and extracted_data != "No upcoming tours":
            existing_event = db_manager.read(extracted_data)

            if not existing_event:
                db_manager.store(extracted_data)
                email_manager.send(
                    message=f"Hey, a new event was found: {extracted_data}"
                )
                print("New event stored and email sent")

        # Pause execution to avoid spamming the target server
        time.sleep(2)
