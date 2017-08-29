from bs4 import BeautifulSoup
from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4

def authenticate():
    
    print('Authenticating...\n')
    reddit = praw.Reddit('zctabot', user_agent = 'web:zcta-bot:v0.1 (by /u/zcta119)')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit

def runBot(reddit):
    print("Getting 250 comments..")
    for comment in reddit.subreddit('test').comments(limit = 5):
        if comment.body == 'What?':
            print(comment.body)
            parent = comment.parent()
            if isinstance(parent, praw.models.Comment):
                text = parent.body
            else:
                text = parent.selftext
            text = "He said \"" + text + " \"!"
            text = text.upper()
            comment.reply(text)
    return

def main():
	reddit = authenticate()
	runBot(reddit)

if __name__ == '__main__':
	main()