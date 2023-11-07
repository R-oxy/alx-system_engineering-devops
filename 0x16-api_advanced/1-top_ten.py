#!/usr/bin/python3
"""Queries the Reddit API and
prints the titles of the first
10 hot posts listed for a given
subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    # Create the Reddit API endpoint URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "my_bot/0.1"}

    # Send an HTTP GET request to the API
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON data and extract the titles of the posts
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        # Invalid subreddit, print None
        print(None)
