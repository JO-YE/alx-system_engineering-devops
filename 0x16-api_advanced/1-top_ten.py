#!/usr/bin/python3
''' a function that queries the Reddit API and
    prints the titles of the first 10 hot posts
'''

import requests


def top_ten(subreddit):
    ''' prints the titles of the first 10 hot posts. '''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'MyApp/1.0'}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        response = response.json().get('data').get('children')
        for entry in response:
            var = entry.get('data').get('title')
            print(var)

    else:
        print(None)
