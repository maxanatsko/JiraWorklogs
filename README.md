# Jira Worklogs Project

This project interacts with a JIRA instance to retrieve worklog data, process it, and optionally send notifications about the script's execution status to a Telegram chat. It also includes functionality for logging.

## Configuration

Before running the scripts, you need to set up a configuration file named `config.ini`. This file should be located in the same directory as the scripts. Here's the structure of the `config.ini` file with the required sections and keys:
```ini
[Auth]
username = YOUR_JIRA_USERNAME
password = YOUR_JIRA_PASSWORD

[Server]
jira_url = YOUR_JIRA_SERVER_URL

[Jira]
jql_query = YOUR_JQL_QUERY
max_results = MAXIMUM_NUMBER_OF_RESULTS

[Results]
directory_path = PATH_WHERE_RESULTS_SHOULD_BE_SAVED
file_name = NAME_OF_THE_OUTPUT_FILE

[Telegram]
bot_token = YOUR_TELEGRAM_BOT_TOKEN
chat_id = YOUR_TELEGRAM_CHAT_ID

[Dev]
log_level = DESIRED_LOG_LEVEL (e.g., INFO, WARN, DEBUG)
```
Replace the placeholders (e.g., `YOUR_JIRA_USERNAME`) with your actual configuration values.

## Setup

To set up the project, you need to:

1. Ensure you have Python installed on your system. The scripts are compatible with the latest Python version.
2. Install required Python libraries: `jira` and `telegram`. You can install these using pip.
3. Place the `config.ini` file with the appropriate configurations in the same directory as the scripts.

```python
pip install jira python-telegram-bot
```

## Usage

Run the `jira_worklogs.py` script to start the process:
```python
python jira_worklogs.py
```
This script will connect to your JIRA instance, retrieve worklog data based on the provided JQL query, process this data, and write the results to a specified file. If configured, it will also send notifications to a Telegram chat.

## Components

The project consists of the following main components:
- `jira_worklogs.py`: The main script to run the JIRA data retrieval and processing.
- `config_reader.py`: Reads configuration settings from `config.ini`.
- `file_writer.py`: Handles writing data to a file.
- `telegram_notifications.py`: Sends notifications to a Telegram chat.
- `logger.py`: Sets up logging for the application.

## Logging

Logs are written to a file named `system_log.log` in the project directory. The log level can be configured in the `config.ini` file under the `[Dev]` section.