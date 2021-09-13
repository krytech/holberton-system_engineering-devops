#!/usr/bin/python3
"""
A script that uses a given employee id, using REST API to return info
about his/her TODO list progress. Exports to JSON.
"""
import json
import requests
from sys import argv


def inquiry_json():
    """Returns API data"""
    url = "https://jsonplaceholder.typicode.com/"
    USER_ID = argv[1]
    user = requests.get(url + "users/{}".format(USER_ID)).json()
    todos = requests.get(url + "todos", params={"userId": USER_ID}).json()
    USERNAME = user.get('username')

    with open("{}.json".format(USER_ID), "w") as jsonfile:
        json.dump({USER_ID: [{
            'task': t.get('title'),
            'completed': t.get('completed'),
            'username': USERNAME
        } for t in todos]}, jsonfile)


if __name__ == "__main__":
    inquiry_json()
