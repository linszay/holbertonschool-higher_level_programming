#!/usr/bin/python3
"""function returns JSON rep of an obj(string)"""
import json


def to_json_string(my_obj):
    "creating function"
    return json.dumps(my_obj)
