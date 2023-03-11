#!/usr/bin/python3
"""fetches url status using only the requests package"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    response = requests.get(url)

    print("Body response:")
    print("\t- type:", response.content.decode('utf-8'))
    print("\t- content:", response.content.decode('utf-8'))
