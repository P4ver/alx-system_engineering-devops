#!/usr/bin/python3
""" to CSV"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_us = 'https://jsonplaceholder.typicode.com/users/' + user
    res_lt = requests.get(url_us)
    """ANYTHING"""
    usr_nm = res_lt.json().get('username')
    task = url_us + '/todos'
    res_lt = requests.get(task)
    tsks = res_lt.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tsks:
            cmpltd = task.get('completed')
            """Complete"""
            titltsk = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, usr_nm, cmpltd, titltsk))
