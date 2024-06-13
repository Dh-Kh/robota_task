# Test Task Mustage

## Prerequisites

Before running this project, ensure that you have the following:

- **Redis**:
  - Make sure that Redis is installed and running on your machine.
  - To install Redis, you can follow the official [Redis Installation Guide](https://redis.io/download).

**Note: This project has been tested on Linux Mint 21.**

## Key Features

### SeleniumRobota Class

The `SeleniumRobota` class is designed as a singleton to manage a single instance of a Selenium WebDriver, ensuring efficient handling and preventing multiple browser instances from running concurrently.

#### Purpose

- Manages a single instance of the Selenium WebDriver (`_driver`) throughout the application.
- Prevents the overhead and potential conflicts of multiple WebDriver instances when performing web automation tasks.

### DatabaseRobota Class

The `DatabaseRobota` class is a singleton that manages a SQLite database connection and provides methods for executing tasks (like inserting and updating data) and retrieving data in a consistent and efficient manner.

#### Purpose

- Ensures only one instance of the database connection (`_connection`) exists at any time.
- Handles database operations (e.g., create table, insert data, update records) with proper error handling to maintain data integrity.

### Excel Module (`excel.py`)

The `excel.py` module is implemented to create Excel files based on data fetched from the `DatabaseRobota` class.

#### Purpose

- Generates Excel files (`data.xlsx`) to store and visualize data fetched from the SQLite database.
- Uses the `openpyxl` library to create and manipulate Excel workbooks and sheets.
- Retrieves data using `DatabaseRobota.retrieve_all()` and formats it into the Excel sheet.

### Telegram Bot (`bot.py`)

The Telegram bot setup using `aiogram` for interacting with users and sending Excel files.

#### Purpose

- Implements a Telegram bot using `aiogram` library to handle commands and interactions.
- Sends `data.xlsx` Excel file to users upon command request.

### Project Structure

```bash
.
├── database
│   ├── __init__.py
│   └── storage.py
├── data.xlsx
├── __init__.py
├── mustage.db
├── Readme.md
├── requirements.txt
├── scheduler_task.py
├── scraper
│   ├── __init__.py
│   └── robota.py
└── tgbot
    ├── bot.py
    ├── excel.py
    └── __init__.py
```

### Setup

1. **Clone the Repository:**
```bash
   git clone https://github.com/Dh-Kh/robota_task.git
```
2. **Create venv and download requirements.txt:**
```bash
    cd robota_task
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
```
3. **Start project:**
```bash
    sh -c "& python3 -m tgbot.bot"
```