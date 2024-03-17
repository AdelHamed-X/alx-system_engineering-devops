#!/usr/bin/python3
""" A Python script that exports todo list info
for a given employee ID to csv file """
import json
import requests
from sys import argv

if __name__ == '__main__':
    filename = 'todo_all_employees.json'

    users = requests.get('https://jsonplaceholder.typicode.com/users')\
        .json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos/',
                         params={'userId': '{}'.format(user_id)}).json()

    data = [{"task": "{}".format(task.get("title")),
                     "completed": task.get("completed"),
                     "username": "{}".format(username)} for task in tasks]

    with open(filename, 'w', newline='')as json_file:
        json.dump({"{}".format(user_id): data}, json_file)
