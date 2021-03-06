import json
from config_reader import config as cr
import os

directory_path = cr.get('Results', 'directory_path')

def write_data_to_file(filename, json_data):
    f = open(os.path.join(directory_path, filename), "w")
    f.write(json.dumps(json_data))
    f.close()