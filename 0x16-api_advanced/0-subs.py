#!/usr/bin/python3
'''module contains function to query subscribers,'''
import requests


def number_of_subscribers(subreddit):
    '''Return the number of subscribers for a given subreddit.'''
    user_agent = {'User-Agent': 'Custom User Agent'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


if __name__ == '__main__':
    subreddit = input("Enter a subreddit: ")
    print(number_of_subscribers(subreddit))
