
# -*- coding: utf-8-*-

# Copyright 2016 g10dras.
__author__ = 'g10dras'

import sys
import time
import re

from tweepy import OAuthHandler
from tweepy import API
from unidecode import unidecode
from client import jasperpath

WORDS = ["TWITTER"]
PRIORITY = 4

# Input is latest retweet, mention, direct message ID
def getNotifications(mic,latestRetweet,latestMention,latestDirectMessage, api):
    try:
        latestRetweets = []
        latestRetweetsID = []
        latestDirectMessages = []
        latestDirectMessagesID = []
        latestMentions = []
        latestMentionsID = []

        mentions = api.mentions_timeline()
        retweets = api.retweets_of_me()
        directMessages = api.direct_messages()

        for mention in mentions:
            if mention.id > latestMention:
                latestMentions.append(mention)
                latestMentionsID.append(mention.id)

        for retweet in retweets:
            if retweet.id > latestRetweet:
                latestRetweets.append(retweet)
                latestRetweetsID.append(retweet.id)

        for directMessage in directMessages:
            if directMessage.id > latestDirectMessage:
                latestDirectMessages.append(directMessage)
                latestDirectMessagesID.append(directMessage.id)

        if len(latestRetweets) > 0:
            mic.say("Latest Retweets are")
            for retweetFinal in latestRetweets:
                mic.say(retweetFinal.text + " by " + retweetFinal.user.screen_name)
            latestRetweetsID.sort()
            latestRetweet = latestRetweetsID[-1]
            retweetsIDFile = open(jasperpath.data('twitter', 'retweetsIDFile.txt'),'w')
            retweetsIDFile.write(str(latestRetweet))
            retweetsIDFile.close()
        else:
            mic.say("You have no retweets")

        if len(latestMentions) > 0:
            mic.say("Latest Mentions are")

            for mentionFinal in latestMentions:
                mic.say(mentionFinal.text + " from " + mentionFinal.user.screen_name)

            latestMentionsID.sort()
            latestMention = latestMentionsID[-1]
            mentionIDFile = open(jasperpath.data('twitter', 'mentionIDFile.txt'),'w')
            mentionIDFile.write(str(latestMention))
            mentionIDFile.close()
        else:
            mic.say("You have no mentions")

        if len(latestDirectMessages) > 0:
            mic.say("Latest Direct Messages are")

            for directMessageFinal in latestDirectMessages:
                mic.say(directMessageFinal.text + " from " + directMessageFinal.user.screen_name)

            latestDirectMessagesID.sort()
            latestDirectMessage = latestDirectMessagesID[-1]
            directMessageIDFile = open(jasperpath.data('twitter', 'directMessageID.txt'),'w')
            directMessageIDFile.write(str(latestDirectMessage))
            directMessageIDFile.close()
        else:
            mic.say("You have no Direct Messages")
    except TweepError as e:
        error = e.reason[0]['message']
        code = e.reason[0]['code']
        mic.say(error + ' Failed to get Notifications.')
        
    return

def getWhatsTrending(mic,api,woeid):
    try:
        data = api.trends_place(woeid)  # 1 for global trends
    except TweepError as e:
        error = e.reason[0]['message']
        code = e.reason[0]['code']
        mic.say(error + ' Getting Global Trends.')
        data = api.trends_place(1)      # 1 for global trends
        
    trends = data[0]['trends']
    for trend in trends:
        name = trend['name']            #Grabs name of each trend
        if name.startswith('#'):
            mic.say(unidecode(name))    #Only grabs hashtags

def getPublicTweets(mic, api):
    try:
        public_tweets = api.home_timeline(count=10)
        idx = 0
        for tweet in public_tweets:
            idx = idx + 1
            text = re.sub(r"(?:\@|https?\://)\S+", "", tweet.text)
            text = text.encode('ascii','ignore').decode('ascii')
            text = ".. " + str(idx) + ") " + text
            mic.say(text)
    except TweepError as e:
        error = e.reason[0]['message']
        code = e.reason[0]['code']
        mic.say(error + ' Failed to get Tweets.')
        
def sendTweet(mic,api):
    try:
        mic.say("What would you like to tweet?")
        tweet = mic.activeListen()
        print "tweet===", tweet
        api.update_status(tweet)
        mic.say("Ok Done.")
    except TweepError as e:
        error = e.reason[0]['message']
        code = e.reason[0]['code']
        mic.say(error + ' Tweet failed.')

def handle(text, mic, profile):
    
    consumer_key = profile['twitter']["TW_CONSUMER_KEY"]
    consumer_secret = profile['twitter']["TW_CONSUMER_SECRET"]
    access_token = profile['twitter']["TW_ACCESS_TOKEN"]
    access_token_secret = profile['twitter']["TW_ACCESS_TOKEN_SECRET"]
    woeid = int(profile['twitter']["WOEID"])
    
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = API(auth)
        myTwitterID = api.me().id
    except Exception as e:
        print e
        mic.say("Connection Error. Twitter service is offline.")
        return
        
    directMessages = api.direct_messages(count=1)
    latestRetweet = 0
    latestMention = 0
    latestDirectMessage = 0

    try:
        directMessageIDFile = open(jasperpath.data('twitter', 'directMessageID.txt'),'r')
        directMessageID = directMessageIDFile.readline()
        latestDirectMessage = int(directMessageID)
        directMessageIDFile.close()
    except IOError:
        if len(directMessages) > 0:
            for directMessage in directMessages:
                latestDirectMessage = directMessage.id
            directMessageIDFile = open(jasperpath.data('twitter', 'directMessageID.txt'),'w')
            directMessageIDFile.write(str(latestDirectMessage))
            directMessageIDFile.close()

    mentions = api.mentions_timeline(count=1)

    try:
        mentionIDFile = open(jasperpath.data('twitter', 'mentionIDFile.txt'),'r')
        latestMentionID = mentionIDFile.readline()
        latestMention = int(latestMentionID)
        mentionIDFile.close()
    except IOError:
        if len(mentions) > 0:
            mentionIDFile = open(jasperpath.data('twitter', 'mentionIDFile.txt'),'w')
            for mention in mentions:
                latestMention = mention.id
            mentionIDFile.write(str(latestMention))
            mentionIDFile.close()

    retweets = api.retweets_of_me(count=1)

    try:
        retweetsIDFile = open(jasperpath.data('twitter', 'retweetsIDFile.txt'),'r')
        retweetsID = retweetsIDFile.readline()
        latestRetweet = int(retweetsID)
        retweetsIDFile.close()
    except IOError:
        if len(retweets) > 0:        
            retweetsIDFile = open(jasperpath.data('twitter', 'retweetsIDFile.txt'),'w')
            for retweet in retweets:
                latestRetweet = retweet.id
            retweetsIDFile.write(str(latestRetweet))
            retweetsIDFile.close()

    if bool(re.search(r'\bTWEET\b', text, re.IGNORECASE)):
        sendTweet(mic, api)

    if bool(re.search(r'\bNOTIFICATIONS\b', text, re.IGNORECASE)):
        getNotifications(mic,latestRetweet,latestMention,latestDirectMessage, api)

    if bool(re.search(r'\bTRENDING\b', text, re.IGNORECASE)):
        getWhatsTrending(mic, api, woeid)
        
    if bool(re.search(r'\bTWEETS\b', text, re.IGNORECASE)):
        getPublicTweets(mic, api)


def isValid(text):
    return any(word in text.upper() for word in WORDS)
