#!/usr/bin/python3
""" A Python script that exports todo list info
for a given employee ID to csv file """
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    filename = '{}.csv'.format(user_id)

    username = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(user_id)).json().get('username')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos/',
                         params={'userId': '{}'.format(user_id)}).json()

    with open(filename, 'w', newline='')as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow([user_id, username,
                                task['completed'], task['title']])
