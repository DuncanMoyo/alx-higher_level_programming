#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests


url = 'https://api.github.com/user'
if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(url, auth=(username, token))
    json_reponse = response.json()
    print(json_response.get('id'))
