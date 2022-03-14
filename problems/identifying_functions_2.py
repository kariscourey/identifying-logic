"""
Requirements:

Given a filename, read the file and convert from
JSON format to native Python data types.

def read_json_data(filename):

    # open and read file

    # decode json format

    return data
"""

import json

def read_json_data(filename):
    pass


def read_json_data_final(filename):
    json_data = None
    with open(filename) as f:
        json_data = f.read()
    if json_data:
        return json.loads(json_data)

    return None

