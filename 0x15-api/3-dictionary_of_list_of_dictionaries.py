#!/usr/bin/python3
"""Script uses a REST API and exports data to json file
"""
import json
import requests
import sys


def convert_to_json():
    """function exports data to json file"""
    api_url = "https://jsonplaceholder.typicode.com/"
    user_url = '{}/users'.format(api_url)
    todo_url = '{}/todos'.format(api_url)

    usr_res = requests.get(user_url)
    usr_data = usr_res.json()

    all_data = {}
    for user in usr_data:
        user_id = user.get('id')
        username = user.get('username')
        todo = requests.get(todo_url, params={'userId': user_id})
        todo_data = todo.json()

        user_task = []
        for todo in todo_data:
            task_title = todo.get('title')
            task_done = todo.get('completed')
            user_task.append({"username": username, "task": task_title,
                              "completed": task_done})
            all_data[user_id] = user_task
    with open('todo_all_employees.json', 'w') as json_s:
        json.dump(all_data, json_s)


if __name__ == '__main__':
    convert_to_json()
