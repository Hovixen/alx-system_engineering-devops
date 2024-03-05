#!/usr/bin/python3
import requests
""" Function queries the Reddit API and prints the titles of the
first 10 hot post listed for a given subreddit
"""


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        post = response.json()

        for posts in post['data']['children']:
            print(posts['data']['title'])
    else:
        print(None)
