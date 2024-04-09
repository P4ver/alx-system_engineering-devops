#!/usr/bin/python3
'''module contains function to query subscribers,'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''Return the num of subscribers,'''
    user = {'User-Agent': 'Chrome/98.0.4758.102'}
    resp = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        res = resp.get('data')
        return res.get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
