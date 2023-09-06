#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response..
"""
import sys
import requests


if __name__ == "__main__":
    post_data = {
        'email': f"{sys.argv[2]}"
    }
    with (
        requests.post(sys.argv[1], data=post_data)
    ) as response:
        print(response.text)
