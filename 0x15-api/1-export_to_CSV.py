#!/usr/bin/python3
"""
A script that uses a given employee id, using REST API to return info
about his/her TODO list progress. Exports to CSV.
"""
import csv
import requests
from sys import argv


def inquiry_csv():
    """Returns API data"""
    url = "https://jsonplaceholder.typicode.com/"
    USER_ID = argv[1]
    user = requests.get(url + "users/{}".format(USER_ID)).json()
    todos = requests.get(url + "todos", params={"userId": USER_ID}).json()
    USERNAME = user.get('username')

    with open("{}.csv".format(USER_ID), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [USER_ID, USERNAME, t.get('completed'), t.get('title')]
        ) for t in todos]


if __name__ == "__main__":
    inquiry_csv()
