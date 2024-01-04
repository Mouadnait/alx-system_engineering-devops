#!/usr/bin/python3
"""
Gets the completed todo list for the user at id and prints to a CSV file.
Usage: ./1-export_to_CSV.py 2
where 2 is a user id
Fake data from "https://jsonplaceholder.typicode.com"
"""
import requests
import sys
import csv


api_url = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":
    users = requests.get(api_url + "/users", params={"id": sys.argv[1]})
    for names in users.json():
        usr_id = names.get('id')
        todo = requests.get(api_url + "/todos", params={"userId": usr_id})
        csv_arr = []
        with open(sys.argv[1] + ".csv", 'a') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for tasks in todo.json():
                writer.writerow([names.get('id'),
                                 names.get('name'),
                                 str(tasks.get('completed')),
                                 tasks.get('title')])
