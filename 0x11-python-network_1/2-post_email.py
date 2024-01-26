#!/usr/bin/python3
"""takes in a URL and an email, 
sends a POST request to the passed URL with the
email as a parameter, and displays
the body of the response (decoded in utf-8)"""
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
