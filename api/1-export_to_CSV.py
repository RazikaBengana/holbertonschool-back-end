#!/usr/bin/python3
"""
This script fetches user and todo data from a JSON placeholder API based on a given user ID,
then writes selected data to a CSV file named after the user ID
"""

import csv
import requests
import sys


if __name__ == "__main__":

    # Fetch the user ID from the command-line arguments
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data from the API and extracts the username
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch todos data for the user from the API
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write user ID, username, todo completion status, and todo title to a CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, t.get("completed"), t.get("title")]) for t in todos]
