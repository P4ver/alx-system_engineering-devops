#!/usr/bin/python3
'''gather employee dt from api.'''


import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            reqst = requests.get('{}/users/{}'.format(REST_API, id)).json()
            tskRq = requests.get('{}/todos'.format(REST_API)).json()
            empName = reqst.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, tskRq))
            compleTsks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    empName,
                    len(compleTsks),
                    len(tasks)
                )
            )
            if len(compleTsks) > 0:
                for task in compleTsks:
                    print('\t {}'.format(task.get('title')))
