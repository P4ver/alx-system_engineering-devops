#!/usr/bin/python3
"""Function to query """
import requests


def number_of_subscribers(subreddit):
    """Return the total """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    results = resp.json().get("data")
    return results.get("subscribers")
