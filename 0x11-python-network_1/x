#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import sys
import requests


if __name__ == '__main__':
    base_url = "https://api.github.com/repos/"
    owner = f"{sys.argv[1]}/"
    repo = f"{sys.argv[2]}/"
    url = base_url + owner + repo + "commits"
    with (
        requests.get(url)
    ) as response:
        response_json = response.json()
        i = 0
        while i < 10 and i < len(response_json):
            sha = response_json[i]['sha']
            author = response_json[i]['commit']['author']['name']
            print(f"{sha}: {author}")
            i += 1
