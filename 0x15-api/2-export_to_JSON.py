#!/usr/bin/python3
'''Records all tasks that are owned by this employee'''

import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_id = int(sys.argv[1])
    user_EP = '{}/users/{}'.format(url, user_id)
    response = requests.get(user_EP).json()
    username = response.get("username")
    tasks_EP = '{}/todos'.format(url)
    tasks = requests.get(tasks_EP).json()
    task_u = {user_id: [{"task": dic.get('title'),
                         'completed': dic.get('completed'),
                         'username': username}
                         for dic in tasks if dic.get("userId") == user_id]}

    # save to a json file
    with open('{}.json'.format(user_id), 'w', encoding='utf-8') as f:
        json.dump(task_u, f)
