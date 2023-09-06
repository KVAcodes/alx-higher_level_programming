#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import sys
import requests


if __name__ == '__main__':
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'KVAcodes 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',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    base_url = "https://api.github.com/repos/"
    owner = f"{sys.argv[1]}/"
    repo = f"{sys.argv[2]}/"
    url = base_url + owner + repo + "commits"
    with (
        requests.get(url, headers=headers)
    ) as response:
        response_json = response.json()
        for i in range(10):
            sha = response_json[i]['sha']
            author = response_json[i]['commit']['author']['name']
            print(f"{sha}: {author}")
