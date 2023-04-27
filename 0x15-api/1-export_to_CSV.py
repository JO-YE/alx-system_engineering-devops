#!/usr/bin/python3
''' python script exporting data in CSV format
    record all task owned by the employee
'''

import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_id = int(sys.argv[1])
    user_EP = '{}/users/{}'.format(url, user_id)
    response = requests.get(user_EP).json()
    username = response.get("name")
    tasks_EP = '{}/todos'.format(url)
    tasks = requests.get(tasks_EP).json()
    task_u = [dic for dic in tasks if dic.get("userId") == user_id]
    task_c = [dic for dic in task_u if dic.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(username, len(task_c), len(task_u)))

    for task in task_c:
        print('\t {}'.format(task.get('title')))
