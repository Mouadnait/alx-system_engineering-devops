#!/usr/bin/python3
#!/usr/bin/python3
"""python script to fetch Rest API for todo lists of employees"""

import json
import requests
import sys


api_url = "https://jsonplaceholder.typicode.com/users"


if __name__ == '__main__':
    resp = requests.get(api_url)
    Users = resp.json()
    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        api_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        api_url = api_url + '/todos/'
        resp = requests.get(api_url)
        tasks = resp.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
            """A little Something"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
