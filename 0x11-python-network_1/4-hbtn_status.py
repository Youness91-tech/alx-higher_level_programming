#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    body_content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body_content)))
    print("\t- content: {}".format(body_content))
