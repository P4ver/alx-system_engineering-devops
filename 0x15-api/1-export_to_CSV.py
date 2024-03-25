#!/usr/bin/python3
""" to CSV"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_us = 'https://jsonplaceholder.typicode.com/users/' + user
    res_lt = requests.get(url_us)
    usr_nm = res_lt.json().get('username')  # Retrieve username from the response
    task = url_us + '/todos'
    res_lt = requests.get(task)
    tsks = res_lt.json()

    with open('{}.csv'.format(user), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write CSV header
        csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        
        # Count the number of tasks
        task_count = 0
        
        for task in tsks:
            cmpltd = task.get('completed')
            titltsk = task.get('title')
            
            # Write task details to CSV
            csv_writer.writerow([user, usr_nm, cmpltd, titltsk])
            task_count += 1
