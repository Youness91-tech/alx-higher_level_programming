#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    error_code = response.status_code
    response_content = response.text

    if error_code >= 400:
        print("Error code: {}".format(error_code))
    else:
        print(response_content)
