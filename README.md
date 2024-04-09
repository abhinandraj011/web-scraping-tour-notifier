# Tour Scraper and Email Notifier

This Python script scrapes a website for upcoming tour information, extracts relevant data, stores it in a SQLite database, and sends email notifications for new tours.

## Features

- **Web Scraping**: Retrieves the source code of a specified URL using the `requests` library.
- **Data Extraction**: Uses the `selectorlib` library to extract specific information from the website source code.
- **SQLite Integration**: Stores extracted tour information in a SQLite database.
- **Email Notification**: Sends email notifications for new tours using SMTP with the `smtplib` library.
- **Continuous Execution**: Runs continuously to check for new tours at regular intervals.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Install dependencies:

    ```bash
    pip install requests selectorlib
    ```

4. Set up email configuration:
    - Update the `send_mail` function in the Python script with your email credentials (SMTP server, sender email, receiver email, etc.).

5. Run the script:

    ```bash
    python main.py
    ```

## Usage

1. **URL Configuration**: Modify the `URL` variable in the Python script to specify the website URL to scrape.
2. **YAML File**: Customize the `extract.yaml` file according to the HTML structure of the website to extract the desired information.
3. **Email Configuration**: Set up your email credentials in the `send_mail` function to receive notifications.
4. **Execution**: The script will continuously scrape the website, extract tour information, store it in the database, and send email notifications for new tours.

## File Structure

- `main.py`: Main Python script for scraping, extracting, storing, and sending notifications.
- `extract.yaml`: YAML configuration file for specifying extraction rules.
- `data.db`: SQLite database file for storing tour information.

## Dependencies

- `requests`
- `selectorlib`
- `sqlite3`

## Contributing

Contributions are welcome! If you'd like to improve the project or add new features, feel free to fork the repository and submit a pull request.
