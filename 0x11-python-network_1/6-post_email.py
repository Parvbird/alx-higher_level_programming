#!/usr/bin/python3
"""Script to
- take in URL and email address
- send POST request to passed URL with email as parameter
- display body of response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)

