#!/usr/bin/python3
import requests
"""
Module to interface with the reddit api
"""


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.

    If not a valid subreddit, print None.
    Invalid subreddits may return a redirect to search results. Ensure
    that you are not following redirects.

    Args:
        subreddit (str): subreddit

    Returns:
        str: titles of the first 10 hot posts
    """
    new_lst = []
    count = 0
    url = 'https://reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'User-Agent': "lala"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        for data in response.json()['data'].get('children'):
            new_lst.append(data['data'].get('title'))
            count += 1
            if count > 9:
                break
        print("\n".join(x for x in new_lst))
    except Exception as err:
        print("None")
