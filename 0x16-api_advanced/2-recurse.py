#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after="ph"):
    """Returns all hot articles for a given subreddit"""
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "ph":
        url = url + "?after={}".format(after)
    r = requests.get(url, headers=headers).json()

    posts = r.get('data', {}).get('children', [])
    if not posts:
        return hot_list
    for i in posts:
        hot_list.append(i.get('data').get('title'))

    after = r.get('data').get('after')
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
