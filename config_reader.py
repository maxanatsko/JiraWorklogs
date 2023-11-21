import configparser
import sys
import os
import logging


def read_config(config_file_path):
    """Read and return the configuration from the given file path."""
    if not os.path.exists(config_file_path):
        logging.error(f"Configuration file not found: {config_file_path}")
        sys.exit(1)

    config = configparser.ConfigParser()
    try:
        config.read(config_file_path)
    except configparser.Error as e:
        logging.error(f"Error reading the configuration file: {e}")
        sys.exit(1)

    return config


if __name__ == "__main__":
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = read_config(config_file)
