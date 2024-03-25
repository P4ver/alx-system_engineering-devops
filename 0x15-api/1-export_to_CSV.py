#!/usr/bin/python3
""" to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    usrid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(usrid)).json()
    usrnm = user.get("username")
    tds = requests.get(url + "todos", params={"userId": usrid}).json()

    with open("{}.csv".format(usrid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [usrid, usrnm, t.get("completed"), t.get("title")]
         ) for t in tds]
