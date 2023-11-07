#!/usr/bin/python3
"""Queries the Reddit API and
returns a list containing the
titles of all hot articles for
a given subreddit.

If no results are found for the
given subreddit, the function
should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles (used for recursion).
        after (str): The Reddit API parameter for pagination.

    Returns:
        list: A list of titles of hot articles.
    """
    # Create the Reddit API endpoint URL
    base_url = "https://www.reddit.com/r/"
    url = f"{base_url}{subreddit}/hot.json?limit=100&after={after}"

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
            hot_list.append(post['data']['title'])

        # Check if there are more pages to fetch
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        # Invalid subreddit or no results, return None
        return None
