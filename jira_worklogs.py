from jira import JIRA
import file_writer
from config_reader import read_config
from telegram_notifications import send_telegram_message as stm
from logger import logger
import datetime
import os


def establish_jira_connection(config):
    """Establishes connection to JIRA."""
    try:
        options = {'server': config.get('Server', 'jira_url'), 'async': True}
        jira = JIRA(options, basic_auth=(config.get('Auth', 'username'), config.get('Auth', 'password')))
        logger.info('Connected to Jira')
        return jira
    except Exception as e:
        logger.error(f'Error connecting to JIRA: {e}')
        raise


def retrieve_issues(jira, config):
    """Retrieves issues from JIRA based on provided JQL query."""
    try:
        jql_query = config.get('Jira', 'jql_query')
        max_results = int(config.get('Jira', 'max_results'))
        issues = jira.search_issues(jql_query, maxResults=max_results)
        logger.info('Issues retrieved from Jira')
        return issues
    except Exception as e:
        logger.error(f'Error retrieving issues from JIRA: {e}')
        raise


def process_worklogs(jira, issues):
    """Processes worklogs from the issues."""
    worklogs = []
    try:
        for issue in issues:
            for worklog in jira.worklogs(issue):
                worklogs.append(worklog.raw)
        logger.info('Worklogs processed')
        return worklogs
    except Exception as e:
        logger.error(f'Error processing worklogs: {e}')
        raise


if __name__ == '__main__':
    stm('Jira worklogs script started ▶')
    start_time = datetime.datetime.now()

    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = read_config(config_file)

    try:
        jira = establish_jira_connection(config)
        issues = retrieve_issues(jira, config)
        worklogs = process_worklogs(jira, issues)
        file_writer.write_data_to_file(config.get('Results', 'file_name'), worklogs, pretty_print=True)
        logger.info('Data written to file')
    except Exception as e:
        logger.error(f'An error occurred: {e}')
    finally:
        end_time = datetime.datetime.now()
        logger.info(f'Jira worklogs script completed in {end_time - start_time}')
