#!/usr/bin/python3
"""fetches url status using only the requests package"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.content))
    print("\t- content:", response.content)
    print("\t- utf8 content:", response.content.decode('utf-8'))
