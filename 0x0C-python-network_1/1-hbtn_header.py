#!/usr/bin/python3
"""displays value found in header of response"""
import urllib.response
import urllib
import sys


if __name__ == "__main__":
    url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')
    print(header)
