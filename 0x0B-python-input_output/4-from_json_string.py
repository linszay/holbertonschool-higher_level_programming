#!/usr/bin/python3
"""returns an object rep by JSON string"""
import json


def from_json_string(my_obj):
    "creating function"
    return json.loads(my_obj)
