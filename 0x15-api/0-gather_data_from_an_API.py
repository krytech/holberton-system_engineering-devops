#!/usr/bin/python3
"""
A script that uses a given employee id, using REST API to return info
about his/her TODO list progress.
"""
import requests
from sys import argv


def inquiry():
    """Returns API data"""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    EMPLOYEE_NAME = user.get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUM_OF_TASKS = 0
    TASK_TITLE = []

    for t in todos:
        if t.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if t.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(t.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    inquiry()
