#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    post_data = {
        'q': sys.argv[1] if len(sys.argv) > 1 else ""
    }
    with (
        requests.post('http://0.0.0.0:5000/search_user', post_data)
    ) as response:
        try:
            response_json = response.json()
        except ValueError:
            print("Not a valid JSON")
        else:
            if not response_json:
                print("No result")
            else:
                print(f"[{response_json['id']}] {response_json['name']}")
