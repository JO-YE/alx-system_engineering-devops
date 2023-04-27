#!/usr/bin/python3
''' python script exporting data in CSV format
    record all task owned by the employee
'''

import csv
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
    task_u = [[user_id, username, dic.get('completed'), dic.get('title')]
              for dic in tasks if user_id == dic.get('userId')]

    # exporting data in CSV format
    with open('{}.csv'.format(user_id), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # write each row of data to csv file
        for row in task_u:
            writer.writerow(row)
