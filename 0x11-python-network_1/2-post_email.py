#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    data = {
        'email': f"{sys.argv[2]}"
    }
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(sys.argv[1], data=post_data)
    with (
        urllib.request.urlopen(request)
    ) as response:
        print(response.read().decode('utf-8'))
