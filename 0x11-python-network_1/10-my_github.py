#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import sys
import requests


if __name__ == '__main__':
    session = requests.Session()
    session.auth = tuple(sys.argv[1:3])

    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    with (
        session.get(f"https://api.github.com/user", headers=headers)
    ) as response:
        response_json = response.json()
        print(response_json.get('id'))
