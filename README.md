<div align="center">

  <h1>🎸 Tour Event Scraper</h1>

  <p>
    A Python automation script that <strong>monitors a website for new tour events</strong> and alerts you the moment one appears.<br />
    Built with web scraping, <strong>SQLite</strong> for deduplication, and <strong>Gmail SMTP</strong> for instant notifications.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/selectorlib-✓-brightgreen?style=for-the-badge" alt="selectorlib" />
    <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
    <img src="https://img.shields.io/badge/SMTP-Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail SMTP" />
    <img src="https://img.shields.io/badge/Automation-✓-orange?style=for-the-badge" alt="Automation" />
  </p>

</div>

<br />

---

## ✨ How It Works

1. The script scrapes the target page every **2 seconds**
2. A CSS selector defined in `extract.yaml` pulls the tour data from the HTML
3. If a new event is found, it's checked against the **SQLite database** to avoid duplicates
4. If it's genuinely new — it gets **stored** and an **email alert** is sent instantly
5. The loop continues indefinitely until manually stopped

---

## 🧠 Under the Hood

### YAML-Driven Extraction
The CSS selector is stored in `extract.yaml` — changing what gets scraped requires no code edits:

```yaml
tours:
  css: '#displaytimer'
```

```python
self.extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
value = self.extractor.extract(source)["tours"]
```

### Deduplication with SQLite
Before storing or alerting, the script checks if the event already exists — so you only get **one email per unique event**, no matter how many times the loop runs:

```python
existing_event = db_manager.read(extracted_data)

if not existing_event:
    db_manager.store(extracted_data)
    email_manager.send(message=f"Hey, a new event was found: {extracted_data}")
```

### Clean Module Architecture
The three responsibilities are split into separate classes under `modules/`, with `__init__.py` keeping imports clean:

```python
from modules import Event, Database, EmailSender
```

---

## 📁 Project Structure

```
Tour-Event-Scraper/
├── modules/
│   ├── __init__.py        # Package init — exposes Event, Database, EmailSender
│   ├── event.py           # Web scraping & CSS extraction logic
│   ├── database.py        # SQLite read/write operations
│   └── email_sender.py    # Gmail SMTP notification sender
├── main.py                # Main loop — orchestrates all three modules
├── extract.yaml           # CSS selector rules for scraping
├── data.db                # SQLite database (auto-created)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AndrewTechTips/Tour-Event-Scraper.git
    cd Tour-Event-Scraper
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set your credentials:**
    ```bash
    export EMAIL="your@gmail.com"
    export PASSWORD="your_gmail_app_password"
    ```
    > ⚠️ Use a [Gmail App Password](https://myaccount.google.com/apppasswords), not your real account password.

4. **Run the scraper:**
    ```bash
    python main.py
    ```

---

## 📬 Contact

* **LinkedIn:** [Andrei Condrea](https://www.linkedin.com/in/andrei-condrea-b32148346)
* **Email:** condrea.andrey777@gmail.com

<p align="center">
  <i>"Never miss a show again." 🎶</i>
</p><div align="center">

  <h1>🎸 Tour Event Scraper</h1>

  <p>
    A Python automation script that <strong>monitors a website for new tour events</strong> and alerts you the moment one appears.<br />
    Built with web scraping, <strong>SQLite</strong> for deduplication, and <strong>Gmail SMTP</strong> for instant notifications.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/selectorlib-✓-brightgreen?style=for-the-badge" alt="selectorlib" />
    <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
    <img src="https://img.shields.io/badge/SMTP-Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail SMTP" />
    <img src="https://img.shields.io/badge/Automation-✓-orange?style=for-the-badge" alt="Automation" />
  </p>

</div>

<br />

---

## ✨ How It Works

1. The script scrapes the target page every **2 seconds**
2. A CSS selector defined in `extract.yaml` pulls the tour data from the HTML
3. If a new event is found, it's checked against the **SQLite database** to avoid duplicates
4. If it's genuinely new — it gets **stored** and an **email alert** is sent instantly
5. The loop continues indefinitely until manually stopped

---

## 🧠 Under the Hood

### YAML-Driven Extraction
The CSS selector is stored in `extract.yaml` — changing what gets scraped requires no code edits:

```yaml
tours:
  css: '#displaytimer'
```

```python
self.extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
value = self.extractor.extract(source)["tours"]
```

### Deduplication with SQLite
Before storing or alerting, the script checks if the event already exists — so you only get **one email per unique event**, no matter how many times the loop runs:

```python
existing_event = db_manager.read(extracted_data)

if not existing_event:
    db_manager.store(extracted_data)
    email_manager.send(message=f"Hey, a new event was found: {extracted_data}")
```

### Clean Module Architecture
The three responsibilities are split into separate classes under `modules/`, with `__init__.py` keeping imports clean:

```python
from modules import Event, Database, EmailSender
```

---

## 📁 Project Structure

```
Tour-Event-Scraper/
├── modules/
│   ├── __init__.py        # Package init — exposes Event, Database, EmailSender
│   ├── event.py           # Web scraping & CSS extraction logic
│   ├── database.py        # SQLite read/write operations
│   └── email_sender.py    # Gmail SMTP notification sender
├── main.py                # Main loop — orchestrates all three modules
├── extract.yaml           # CSS selector rules for scraping
├── data.db                # SQLite database (auto-created)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AndrewTechTips/Tour-Event-Scraper.git
    cd Tour-Event-Scraper
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set your credentials:**
    ```bash
    export EMAIL="your@gmail.com"
    export PASSWORD="your_gmail_app_password"
    ```
    > ⚠️ Use a [Gmail App Password](https://myaccount.google.com/apppasswords), not your real account password.

4. **Run the scraper:**
    ```bash
    python main.py
    ```

---

## 📬 Contact

* **LinkedIn:** [Andrei Condrea](https://www.linkedin.com/in/andrei-condrea-b32148346)
* **Email:** condrea.andrey777@gmail.com

<p align="center">
  <i>"Never miss a show again." 🎶</i>
</p>