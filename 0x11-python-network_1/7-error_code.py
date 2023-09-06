#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    with (
        requests.get(sys.argv[1])
    ) as response:
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
