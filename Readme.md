# Test Task Mustage

## Prerequisites

Before running this project, ensure that you have the following:

- **Docker**:
  - Make sure Docker and Docker Compose are installed on your system.

**Note: This project has been tested on Linux Mint 21.**

## Key Features

# SeleniumRobota and DatabaseRobota

This project includes two classes, `SeleniumRobota` and `DatabaseRobota`, which handle web automation and database operations respectively.

## SeleniumRobota Class

The `SeleniumRobota` class manages a Selenium WebDriver instance to perform web automation tasks efficiently.

### Purpose

- **WebDriver Management**: Initializes and manages a Selenium WebDriver instance.
- **Web Automation**: Navigates to URLs, interacts with web elements, and extracts data.
- **Headless Operation**: Runs the browser in headless mode for efficiency

#### Purpose

- Ensures only one instance of the database connection (`_connection`) exists at any time.
- Handles database operations (e.g., create table, insert data, update records) with proper error handling to maintain data integrity.

## DatabaseRobota Class
The DatabaseRobota class manages a PostgreSQL database connection, providing methods for executing database tasks such as inserting and updating data, and retrieving records.

#### Purpose

- Database Connection Management: Establishes and maintains a PostgreSQL database connection.
- Data Operations: Handles creation of tables, data insertion, and record updates.
- Data Integrity: Ensures data consistency and integrity through robust error handling and transactions.

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

### Celery (`celery_app.py`)

This extension enables you to run the periodic tasks every hour.

### Project Structure

```bash
.
├── backend
│   ├── celeryconfig.py
│   ├── database
│   │   ├── __init__.py
│   │   └── storage.py
│   ├── Dockerfile
│   ├── __init__.py
│   ├── requirements.txt
│   ├── scraper
│   │   ├── __init__.py
│   │   └── robota.py
│   ├── tasks.py
│   └── tgbot
│       ├── bot.py
│       ├── excel.py
│       └── __init__.py
├── docker-compose.yml
└── Readme.md


```

### Setup

1. **Clone the Repository:**
```bash
   git clone https://github.com/Dh-Kh/robota_task.git
```
2. **Build project:**
```bash
    docker-compose build
    docker-compose up -d
```
3. **Start project:**
```bash
    docker-compose run app sh -c "celery -A tasks worker --loglevel=info --beat & python3 -m tgbot.bot"
```

4. **Start the Bot**: If you haven't already, start the bot by searching for `https://t.me/MustageTestBotBot` on Telegram and clicking on "Start".

5. **Use the Command**: Once the bot is started, open a chat with it and type the following command:

```bash
    /get_today_statistic 
```

6. **Useful commands**:
```bash
    docker-compose exec pgdb psql -h localhost -U postgres
    docker-compose down -v
```