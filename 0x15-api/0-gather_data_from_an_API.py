#!/usr/bin/python3
"""
Gets the completed todo list for the user at id.
Usage: ./0-gather_data_from_an_API.py 2
where 2 is the user id of Ervin Howell.
Fake data from "https://jsonplaceholder.typicode.com"
"""
import re
import requests
import sys


api_url = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    id = int(sys.argv[1])
    req = requests.get('{}/users/{}'.format(api_url, id)).json()
    task_req = requests.get('{}/todos'.format(api_url)).json()
    emp_name = req.get('name')
    tasks = list(filter(lambda x: x.get('userId') == id, task_req))
    completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
    print(
        'Employee {} is done with tasks({}/{}):'.format(
            emp_name,
            len(completed_tasks),
            len(tasks)
        )
    )
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
