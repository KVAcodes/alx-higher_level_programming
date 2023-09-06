#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).manage
urllib.error.HTTPError exceptions and print: Error code: followed
by the HTTP status code.
"""
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    try:
        with (
            urllib.request.urlopen(sys.argv[1])
        ) as response:
            content_byte = response.read()
            print(content_byte.decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
