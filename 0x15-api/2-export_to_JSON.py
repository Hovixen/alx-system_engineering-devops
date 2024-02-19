#!/usr/bin/python3
"""Script uses a REST API and exports data to json file
"""
import json
import requests
import sys


def convert_to_json(user_id):
    """function exports data to json file"""
    api_url = "https://jsonplaceholder.typicode.com/"
    user = '{}/users/{}'.format(api_url, user_id)
    todo_url = '{}/todos?userId={}'.format(api_url, user_id)

    usr_res = requests.get(user)
    usr_data = usr_res.json()
    user_name = usr_data.get('username')

    todo_res = requests.get(todo_url)
    todo_data = todo_res.json()

    all_data = []
    for data in todo_data:
        data = {"task": data.get('title'), "completed": data.get('completed'),
                "username": user_name}
        all_data.append(data)

    json_file = '{}.json'.format(user_id)

    with open(json_file, 'w') as json_s:
        json.dump({user_id: all_data}, json_s)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee Id>".format(sys.argv[0]))
        sys.exit(1)
    user_id = int(sys.argv[1])
    convert_to_json(user_id)
