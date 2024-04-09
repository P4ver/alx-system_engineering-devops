#!/usr/bin/python3
"""module contains function to query subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the num of subscribers,"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Chrome"
    }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    res = resp.json().get("data")
    return res.get("subscribers")
