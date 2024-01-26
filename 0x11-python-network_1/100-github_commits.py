#!/usr/bin/python3
""" takes 2 arguments in order to solve this challenge. """
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    request = requests.get(url)
    response_json = request.json()
    for idx in response_json[:10]:
        commit_sha = idx.get("sha")
        commit_author = idx.get("commit").get("author").get("name")
        print("{}: {}".format(commit_sha, commit_author))
