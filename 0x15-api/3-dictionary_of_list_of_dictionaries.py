#!/usr/bin/python3
"""
A script that exports all employee information to JSON format.
"""
import json
import requests


def inquiry_all_json():
    """Returns API data"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get('id'): [{
                'task': t.get('title'),
                'completed': t.get('completed'),
                'username': u.get('username')
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get('id')}).json()]
            for u in users}, jsonfile)


if __name__ == "__main__":
    inquiry_all_json()
