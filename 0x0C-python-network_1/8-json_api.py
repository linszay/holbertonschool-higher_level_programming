#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as
a parameter
"""
import requests
import sys

if __name__ == "__name__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    info = {"q": letter}

    req = requests.post(url, data=info)

    try:
        json_data = req.json()
        if json_data:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")