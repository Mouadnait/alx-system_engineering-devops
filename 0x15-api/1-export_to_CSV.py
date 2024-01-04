#!/usr/bin/python3
"""
Gets the completed todo list for the user at id and prints to a CSV file.
Usage: ./1-export_to_CSV.py 2
where 2 is a user id
Fake data from "https://jsonplaceholder.typicode.com"
"""
import requests
import sys
import json


api_url = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":
    user_id = sys.argv[1]
    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(api_url, user_id)
    # get info from api
    response = requests.get(user_url)
    # pull data from api
    data = response.text
    # parse the data into JSON format
    data = json.loads(data)
    # extract user data, in this case, username of employee
    user_name = data[0].get('username')
    # get user info about todo tasks
    tasks_url = '{}/todos?userId={}'.format(api_url, user_id)
    # get info from api
    response = requests.get(tasks_url)
    # pull data from api
    tasks = response.text
    # parse the data into JSON format
    tasks = json.loads(tasks)
    # build the csv
    builder = ""
    for task in tasks:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            user_name,
            task['completed'],  # or use get method
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)
