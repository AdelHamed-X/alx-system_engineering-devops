#!/usr/bin/python3
""" A script that interacts with reddit api """
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ gets the subs number of a subreddit """
    headers = {"User-Agent": "api/1.0 (by /u/AdelHamed-X)"}
    resp = requests.get(f'https://www.reddit.com/r/{subreddit}/about',
                        headers=headers)

    if resp.status_code == 200:
        try:
            result = resp.json().get('data')
            return result.get('subscribers')
        except Exception:
            pass
    else:
        return 0
