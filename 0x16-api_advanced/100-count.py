#!/usr/bin/python3
""" Count it."""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively count and print the occurrences of given keywords
    in hot article titles of a subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of keywords to count occurrences.
        after (str): A token used for paginating through Reddit API responses.
        counts (dict): A dictionary to store keyword counts.

    Returns:
        None
    """
    if not word_list:
        return

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        base_url = "https://www.reddit.com/r/"
        url = f"{base_url}{subreddit}/hot.json?limit=100&after={after}"

    headers = {'User-Agent': 'my_bot/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            count = title.count(word)
            if word not in counts:
                counts[word] = count
            else:
                counts[word] += count

    next_page = data['data']['after']
    if next_page is not None:
        count_words(subreddit, word_list, next_page, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>"
              .format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
