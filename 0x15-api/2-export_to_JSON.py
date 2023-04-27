#!/usr/bin/python3
'''Records all tasks that are owned by this employee'''

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
    task_u = [dic for dic in tasks if dic.get("userId") == user_id]
