#!/usr/bin/python3
'''function top_ten'''
import requests
from sys import argv


def top_ten(subreddit):
    '''returns the top ten posts'''
    usr = {'User-Agent': 'Chrome/98.0.4758.102'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=usr)
    if response.status_code == 200:
        try:
            data = response.json()
            for pst in data.get('data').get('children'):
                print(pst.get('data').get('title'))
        except Exception as e:
            print("Error parsing JSON:", e)
    else:
        print("Error:", response.status_code)
        print("Response content:", response.content)


if __name__ == "__main__":
    top_ten(argv[1])
