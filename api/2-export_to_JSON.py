#!/usr/bin/python3
"""A script to fetch user details and their tasks from a JSON API and store the data in a JSON file"""

import json
import requests
import sys


if __name__ == "__main__":

    user_id = sys.argv[1]  # Read user ID from command line arguments
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user details by user ID
    user = requests.get(url + "users/{}".format(user_id)).json()

    username = user.get("username")  # Extract username from user details

    # Fetch todo items for the user
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write the user's todos to a JSON file named after the user ID
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),           # Title of the todo item
            "completed": t.get("completed"),  # Completion status of the todo item
            "username": username              # Username of the user
        } for t in todos]}, jsonfile)
