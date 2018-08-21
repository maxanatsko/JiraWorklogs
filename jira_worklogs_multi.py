from jira import JIRA
import file_writer
from config_reader import config as cr
from telegram_notifications import send_telegram_message as stm
from logger import logger
import concurrent
import time, random
import joblib

stm("Jira worklogs script started ▶")
try:
    # logging
    logger.info('Process Started')
    print('Started logging')

    # Get data from config file
    username = cr.get('Auth', 'username')
    password = cr.get('Auth', 'password')
    jira_url = cr.get('Server', 'jira_url')
    jql_query = cr.get('Jira', 'jql_query')
    max_results = cr.get('Jira', 'max_results')
    file_name = cr.get('Results', 'file_name')
    print('Finished reading config file')

    options = {
        'server': jira_url,
        'async': True}

    print('Establishing connection to Jira')
    jira = JIRA(options, basic_auth=(username, password))

    print('Connected to Jira')

    print('Retrieving issues from Jira')
    issue_keys_list = jira.search_issues(jql_query, maxResults=300, startAt=0) + jira.search_issues(jql_query, maxResults=max_results, startAt=300)

    worklog_ids = []
    worklogs = []

    print('Retrieving worklogs from the issues')
    for ikl in issue_keys_list:
        worklog_ids = jira.worklogs(ikl)
        for wk in worklog_ids:
            worklogs.append(wk.raw)

    print('Finished getting worklogs')
    print('Writing data to disk')
    file_writer.write_data_to_file(file_name, worklogs)

    # finish timestamp in the log
    logger.info('Process Finished')
    stm("Jira worklogs script finished successfully ✅")
except:
    stm("Jira worklogs script terminated with error ⛔")