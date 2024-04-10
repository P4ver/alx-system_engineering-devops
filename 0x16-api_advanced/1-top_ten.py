#!/usr/bin/python3
'''function top_ten'''
import requests
from sys import argv


def top_ten(subreddit):
    '''returns the top ten posts'''
    usr = {'User-Agent': 'Chrome/98.0.4758.102'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=usr).json()
    try:
        for pst in url.get('data').get('children'):
            print(pst.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
