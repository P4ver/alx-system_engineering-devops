#!/usr/bin/python3
"""module contains function to query a list of all hot posts"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "Chrome/98.0.4758.102"
    }
    param = {
        "after": after,
        "count": count,
        "limit": 100
    }
    resp = requests.get(url, headers=header, params=param,
                        allow_redirects=False)
    if resp.status_code == 404:
        return None

    reslt = resp.json().get("data")
    after = reslt.get("after")
    count += reslt.get("dist")
    for cnt in reslt.get("children"):
        hot_list.append(cnt.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
