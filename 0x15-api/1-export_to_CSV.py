#!/usr/bin/python3
"""Script uses a REST API and converts data to csv
"""
import csv
import requests
import sys


def convert_to_csv(user_id):
    """function converts data to csv"""
    api_url = "https://jsonplaceholder.typicode.com/"
    user = '{}/users/{}'.format(api_url, user_id)
    todo_url = '{}/todos?userId={}'.format(api_url, user_id)

    usr_res = requests.get(user)
    usr_data = usr_res.json()
    user_name = usr_data.get('name')

    todo_res = requests.get(todo_url)
    todo_data = todo_res.json()

    all_data = []
    for data in todo_data:
        all_data.append([data.get('userId'), user_name,
                        data.get('completed'), data.get('title')])

    csv_file = '{}.csv'.format(user_id)

    with open(csv_file, 'w', newline='') as user_csv:
        user_write = csv.writer(user_csv, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for row in all_data:
            user_write.writerow(row)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee Id>".format(sys.argv[0]))
        sys.exit(1)
    user_id = int(sys.argv[1])
    convert_to_csv(user_id)
