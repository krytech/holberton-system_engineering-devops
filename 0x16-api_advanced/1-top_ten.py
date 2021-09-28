#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Returns the top ten hot post titles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    r = requests.get(url, headers=headers).json()
    posts = r.get('data', {}).get('children', [])
    if not posts:
        print('None')
    for i in posts:
        print(i.get('data').get('title'))
