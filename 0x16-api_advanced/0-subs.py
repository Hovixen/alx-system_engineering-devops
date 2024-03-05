#!/usr/bin/python3
""" Function queries Reddit API and returns the number of
subscribers(not active, but total) of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subs_info = response.json()
        return subs_info['data']['subscribers']
    else:
        return 0
