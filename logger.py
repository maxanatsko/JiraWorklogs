import logging
import argparse
import os
from config_reader import read_config


# Read configuration
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config = read_config(config_file)

# Adding command-line arguments for log level
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="you can pass --log (-l) argument: INFO/WARN/DEBUG", type=str)
args = parser.parse_args()

# Setting log level from config file or command line argument
log_level = config.get('Dev', 'log_level') if config.get('Dev', 'log_level') else "INFO"
if args.log:
    log_level = args.log

# Setting up the logger
logger = logging.getLogger()
logger.setLevel(log_level.upper())

handler = logging.FileHandler('system_log.log', 'a+', 'utf-8')
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
