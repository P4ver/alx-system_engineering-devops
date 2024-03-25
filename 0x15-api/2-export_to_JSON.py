#!/usr/bin/python3
"""to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    usrid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(usrid)).json()
    username = user.get("username")
    tds = requests.get(url + "todos", params={"userId": usrid}).json()

    with open("{}.json".format(usrid), "w") as jsonfile:
        json.dump({usrid: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in tds]}, jsonfile)
