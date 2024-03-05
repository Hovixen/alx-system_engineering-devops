#!/usr/bin/python3
""" Function queries the Reddit API recursively and returns a list
containing all titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, after=None, articles=None):
    if articles is None:
        articles = []

    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        for article in data['data']['children']:
            articles.append(article['data']['title'])
        after = data['data']['after']

        if after is not None:
            recurse(subreddit, after, articles)
    else:
        return None
    return articles
