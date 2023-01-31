#!/usr/bin/python3
"""creates an obj from a 'JSON file'"""
import json


def load_from_json_file(filename):
    "creating function"
    with open(filename, "r") as f:
        return json.load(f)
