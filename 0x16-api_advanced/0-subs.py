#!/usr/bin/python3
'''  a function that queries the Reddit API
    and returns the number of subscribers for a guven subreddit.
'''

import requests


def number_of_subscribers(subreddit):
    ''' returns the number of subscriber. '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'MyApp/1.0'}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        count = response.get('data').get('subscribers')
        return count
    return 0
