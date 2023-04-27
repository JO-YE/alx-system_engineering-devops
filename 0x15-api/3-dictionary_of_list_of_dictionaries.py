#!/usr/bin/python3
'''Records all tasks from ALL employee'''

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_EP = '{}/users'.format(url)
    users = requests.get(user_EP).json()
    tasks_EP = '{}/todos'.format(url)
    tasks = requests.get(tasks_EP).json()
    task_u = {user.get('id'): [{"username": user.get('username'),
                                'task': dic.get('title'),
                                'completed': dic.get('completed')}
                               for dic in tasks
                               if dic.get("userId") == user.get('id')]
              for user in users}

    # save to a json file
    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(task_u, f)
