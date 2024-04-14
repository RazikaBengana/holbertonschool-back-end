#!/usr/bin/python3
"""
This script retrieves user data from a JSON placeholder API and stores each user's tasks,
including task title, completion status, and username, in a JSON file named 'todo_all_employees.json'
"""

import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    # Make a GET request to retrieve a list of users and parses the JSON response
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        # Dump user tasks data to a JSON file where each user's tasks are mapped to their user ID
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),             # Title of the task
                "completed": t.get("completed"),    # Completion status of the task
                "username": u.get("username")       # Username of the user
            } for t in requests.get(url + "todos",  # Make another GET request to retrieve tasks
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
