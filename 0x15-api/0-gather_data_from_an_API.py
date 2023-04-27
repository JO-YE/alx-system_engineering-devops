#!/usr/bin/python3
'''using this REST API, for a given employee ID, returns information
   about his/her TODO list progress
'''

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
