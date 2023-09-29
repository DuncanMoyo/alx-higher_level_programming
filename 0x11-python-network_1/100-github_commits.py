#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)"""

import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Unable to reach the API endpoint")
    else:
        commits = response.json()
        for commit in commits[:10]:
            print("{}: {}".format(commit.get('sha'), commit.get('commit').get('author').get('name')))
