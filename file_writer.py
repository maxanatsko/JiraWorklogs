import json
import os
import logging
from config_reader import read_config

# Assuming config.ini is in the same directory as this script
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config = read_config(config_file)
directory_path = config.get('Results', 'directory_path')

def write_data_to_file(filename, json_data, pretty_print=False):
    """Writes the given JSON data to a file."""
    full_path = os.path.join(directory_path, filename)
    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            if pretty_print:
                f.write(json.dumps(json_data, indent=4))
            else:
                f.write(json.dumps(json_data))
    except OSError as e:
        logging.error(f"Error writing to file {filename}: {e}")
        raise