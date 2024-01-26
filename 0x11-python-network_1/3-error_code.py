#!/usr/bin/python3
""" takes in a URL,sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_content = response.read()
            decoded_response = response_content.decode('utf-8')
            print(decoded_response)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
