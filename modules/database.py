import sqlite3
from typing import List, Tuple


class Database:
    """Handles all SQLite database operations for events."""

    def __init__(self, database_path: str = "data.db"):
        self.database_path = database_path

    def _get_connection(self):
        """Returns a new connection to the database"""
        return sqlite3.connect(self.database_path)

    def store(self, extracted: str) -> None:
        """Stores a new event in the database"""

        row = [item.strip() for item in extracted.split(",")]

        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
            connection.commit()

    def read(self, extracted: str) -> List[Tuple]:
        """Checks if an event already exists in the database"""
        row = [item.strip() for item in extracted.split(",")]
        band, city, date = row

        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM events WHERE band=? AND city=? AND date=?",
                (band, city, date),
            )
            return cursor.fetchall()
