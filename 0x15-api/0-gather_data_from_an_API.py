#!/usr/bin/python3
"""Script uses a REST API to prints information about a user TODO
list progress
"""
import requests
import sys


def get_user_info(user_id):
    """function prints user TODO list progress"""
    api_url = "https://jsonplaceholder.typicode.com/"
    user = '{}/users/{}'.format(api_url, user_id)
    todo_url = '{}/todos?userId={}'.format(api_url, user_id)

    usr_res = requests.get(user)
    usr_data = usr_res.json()
    user_name = usr_data.get('name')

    todo_res = requests.get(todo_url)
    todo_data = todo_res.json()

    tasks = []
    for task in todo_data:
        if task.get('completed') is True:
            tasks.append(task)
    all_task = len(todo_data)
    completed_task = len(tasks)
    progress = '{}/{}'.format(completed_task, all_task)

    print('Employee {} is done with tasks ({})'.format(user_name, progress))
    for task in tasks:
        print('\t {}'.format(task.get('title')))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee Id>".format(sys.argv[0]))
        sys.exit(1)
    user_id = int(sys.argv[1])
    get_user_info(user_id)
