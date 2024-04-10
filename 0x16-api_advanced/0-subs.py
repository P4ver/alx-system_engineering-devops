#!/usr/bin/python3
'''module contains function to query subscribers,'''
import requests


def number_of_subscribers(subreddit):
    '''Return the number of subscribers for a given subreddit.'''
    # Set a custom User-Agent to avoid 429 (Too Many Requests) errors
    user_agent = {'User-Agent': 'Custom User Agent'}

    # Construct the URL for the subreddit's about.json
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Make the request to the Reddit API
    response = requests.get(url, headers=user_agent)

    # Check if the response is successful
    if response.status_code == 200:
        try:
            # Extract the number of subscribers from the JSON response
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            # If the 'subscribers' key is not found in the response, return 0
            return 0
    elif response.status_code == 404:
        # If the subreddit does not exist, return 0
        return 0
    else:
        # If there is any other issue with the request, return 0
        return 0


# Example usage:
if __name__ == '__main__':
    subreddit = input("Enter a subreddit: ")
    print(number_of_subscribers(subreddit))
