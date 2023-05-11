#!/usr/bin/python3
''' '''

import requests


def recurse(subreddit, hot_list=[], after=None):
    ''' '''
    url = 'https://www.reddit.com/r/{}/hot.json?{}'.format(subreddit, after)
    header = {'User-Agent': 'Joye'}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        after = response.json().get('data').get('after')
        response = response.json().get('data').get('children')
        for entry in response:
            hot_list.append(entry.get('data').get('title'))
        if after:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    return (None)
