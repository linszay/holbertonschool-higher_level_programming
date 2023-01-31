#!/usr/bin/python3
"""writes obj to txt file using JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    "creating function"
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
