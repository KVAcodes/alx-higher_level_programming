#!/usr/bin/python3
"""This is a script that fetches https://alx-intranet.hbtn.io/status.
"""
import urllib.request


if __name__ == "__main__":
    with (
        urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
    ) as response:
        content_byte = response.read()
        formatted_output = (
            "Body response:\n"
            "    - type: {}\n"
            "    - content: {}\n"
            "    - utf8 content: {}"
        ).format(type(content_byte), content_byte,
                 content_byte.decode(encoding="utf-8"))
        print(formatted_output)
