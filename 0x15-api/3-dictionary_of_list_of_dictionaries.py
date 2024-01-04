#!/usr/bin/python3
"""
python script to fetch Rest API for todo lists of employees
"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":
    # get users info e.g https://jsonplaceholder.typicode.com/users
    users_url = '{}/users'.format(base_url)
    # get info from api
    response = requests.get(users_url)
    # pull data from api
    data = response.text
    # parse the data into JSON format
    data = json.loads(data)
    # extract users data
    builder = {}
    for user in data:
        user_id = user.get('id')
        user_name = user.get('username')
        dict_key = str(user_id)
        builder[dict_key] = []
        # get user info about todo tasks
        tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
        # get info from api
        response = requests.get(tasks_url)
        # pull data from api
        tasks = response.text
        # parse the data into JSON format
        tasks = json.loads(tasks)
        for task in tasks:
            json_data = {
                "task": task['title'],  # or use get method
                "completed": task['completed'],
                "username": user_name
            }
            # append dictionary key to the dictionary
            builder[dict_key].append(json_data)
    # write the data to the file
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
