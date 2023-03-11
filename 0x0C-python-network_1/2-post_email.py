#!/usr/bin/python3
"""
script takes in URL & email, sends a POST request
to the passed URL with the email as a param, and
displays the body of the response(decode in utf-8)
"""
import sys
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode()
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
