#!/usr/bin/python3
"""
Gets the completed todo list for the user at id.
Usage: ./0-gather_data_from_an_API.py 2
where 2 is the user id of Ervin Howell.
Fake data from "https://jsonplaceholder.typicode.com"
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    # URL for the REST API
    api_url = f'https://jsonplaceholder.typicode.com'
    # Make a GET request to the API
    users = requests.get(api_url + "/users", params={"id": sys.argv[1]})
    # Check if the request was successful (status code 200)
    names = users.json()
    # Extract employee name
    employee_name = names[0].get('name')
    # Extract User ID
    user_id = names[0].get('id')
    # Count the number of completed tasks
    users_todo = requests.get(api_url + "/todos", params={"userId": user_id})
    todos = users_todo.json()
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)
    # Display employee information
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))
    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    # Get employee ID from command-line arguments
    employee_id = int(sys.argv[1])
    # Call the function to get and display employee TODO list progress
    get_employee_todo_progress(employee_id)
