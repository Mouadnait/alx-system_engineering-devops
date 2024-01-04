#!/usr/bin/python3
"""
Gets the completed todo list for the user at id and prints to a JSON file.
Usage: ./1-export_to_JSON.py 2
where 2 is a user id
Fake data from "https://jsonplaceholder.typicode.com"
"""
import json
import requests
import sys


def get_employee(employee_id, api_url):
    # get info from the API
    response = requests.get(api_url + "/users", params={"id": employee_id})
    for names in response.json():
        todo = requests.get(api_url + "/todos", params={"userId": employee_id})
        task = todo.json()
        completed_tasks = [todo for todo in task if todo['completed']]
        # Prepare data for JSON export
        json_data = {
            "USER_ID": [
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": names.get('name')
                }
                for task in completed_tasks
            ]
        }
        # Create JSON file with user ID as the filename
        filename = f"{employee_id}.json"
        with open(filename, mode='w') as file:
            json.dump(json_data, file, indent=2)


if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(sys.argv[1])
    get_employee(employee_id, api_url)
