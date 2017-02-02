# -*- coding: utf-8-*-

# Copyright 2016 g10dras.
__author__ = 'g10dras'

import re
import feedparser
from Unidecode import unidecode

WORDS = ["JASPER", "SUPPORT", "FORUM"]

def getJasperSupportForum(maxResults=5):

    JASPER_FORUM_URL = "https://groups.google.com/forum/feed/jasper-support-forum/msgs/rss.xml?num={0}".format(str(maxResults))
    
    feedparser.RESOLVE_RELATIVE_URIS = 0
    feed = feedparser.parse(JASPER_FORUM_URL)

    if feed.bozo == 1:
        top_posts = "Seems Jasper Support Forum is down."
    else:
        top_posts = "Here are the top {0} posts... ".format(str(maxResults))
        idx = 1
        for item in feed['items']:
            title = item["title"]
            author = item["author"]
            if 'Re:' in title.split():
                title = re.sub('Re:', '', title)
                top_posts += "{0}{1} {2}. Reply to post {3}. ".format(str(idx), ")", unidecode(author), title)
            else:
                top_posts += "{0}{1} {2}. Posts {3}. ".format(str(idx), ")", unidecode(author), title)
            idx += 1

    return top_posts

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    try:
        maxResults = 5
        top_posts = getJasperSupportForum(maxResults)
        mic.say(top_posts)
    except Exception:
        mic.say('Service is down or Check Internet Connection.')
    return

def isValid(text):
    """
        Returns True if the input is related to jokes/humor.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text.upper() for word in WORDS)
