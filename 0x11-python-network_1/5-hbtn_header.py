#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response, using the requests package.
"""
import requests
import sys


if __name__ == "__main__":
    with (
        requests.get(sys.argv[1])
    ) as response:
        print(response.headers.get('X-Request-Id'))
