#!/usr/bin/python3
"""
This script retrieves user and task information from a JSON placeholder API
and prints completed tasks for a specified user
"""

import requests
from requests import get
import sys
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information based on the user ID provided as a command line argument
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # Fetch all tasks for the specified user
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # List comprehension to filter and gather titles of completed tasks
    completed = [title.get("title") for title in todos

                 if title.get("completed") is True]
    # Output the name of the user and the count of completed vs. total tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print each completed task title
    [print("\t {}".format(c)) for c in completed]
