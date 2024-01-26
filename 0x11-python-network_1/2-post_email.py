#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response."""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    encoded_data = urllib.parse.urlencode(data).encode('ascii')

    request = urllib.request.Request(url, data=encoded_data, method='POST')
    with urllib.request.urlopen(request) as response:
        response_content = response.read()
        decoded_response = response_content.decode('utf-8')
        print(decoded_response)
