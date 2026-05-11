import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


class Event:
    """Handles web scraping and data extraction"""

    def __init__(self, yaml_path: str = "extract.yaml"):
        # Initialize the extractor only once to optimize performance
        self.extractor = selectorlib.Extractor.from_yaml_file(yaml_path)

    def scrape(self, url: str = URL) -> str:
        """Scrape the page source from the URL"""

        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"There was an error accessing the site {e}")
            return ""

    def extract(self, source: str) -> str:
        """Extract the specific tour data from the page source using the YAML rules"""
        value = self.extractor.extract(source)["tours"]
        return value
