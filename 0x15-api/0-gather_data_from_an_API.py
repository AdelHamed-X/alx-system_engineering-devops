#!/usr/bin/python3
""" A Python script that, using this REST API, for a given employee ID """

from sys import argv
import requests

user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(argv[1])).json()
tasks = requests.get('https://jsonplaceholder.typicode.com/todos/',
                     params={'userId': '{}'.format(argv[1])}).json()

done_tasks_title = [task['title'] for task in tasks if task['completed']]
done_tasks = len(done_tasks_title)

print('Employee {} is done with tasks({}/{}):'
      .format(user_info.get('name'), done_tasks , len(tasks)))

[print('\t {}'.format(task)) for task in done_tasks_title]
