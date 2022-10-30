import random
import time
import tweepy
from datetime import datetime, timedelta


#returns variable that contains the time 10 minutes ago
def Time():
    curTime = datetime.utcnow()
    nowMinusTen = curTime - timedelta(minutes=20)
    return nowMinusTen

#likes whatever tweet is fed to the function
def LikeTweet(tweetID):

    client.like(tweetID)

#tweets whatever is fed as input   
def Tweet(text):
    text = str(text)
    client.create_tweet(text=text)

#replies to whatever tweet is fed as input
def Reply(text, replyID):
    text = str(text)
    client.create_tweet(text=text, in_reply_to_tweet_id=replyID)

#Does what you'd think
def GetUser():
    username = "tracktheirmoney"
    user = client.get_user(username=username)
    return user.data.id

#def ShowUserTweets(userID):
    tweet = client.get_users_tweets(userID)
    print("Your Tweets: ")
    for tweet in tweet.data:
        print(tweet)
    print()

#displays all mentions starting from ten minutes prior to running script
def ShowMentions(userID):
    mentions = client.get_users_mentions(userID, expansions=["author_id"], start_time=Time())
    if mentions.data == None:
        print("no mentions?")
    else:
        listOfMentions = []
        print("Your Mentions:")
        for mentions in mentions.data:
            print(mentions)
            print()
            listOfMentions.append(mentions.id)
        return listOfMentions

#gets text from all found tweets & puts them into an array of strings
def GetTweetText(userID):
    mentions = client.get_users_mentions(userID, expansions=["author_id"], start_time=Time())
    tweetText = []
    if mentions.data != None:
        listOfMentions = []
        for mentions in mentions.data:
            tweetText.append(mentions.text[17:263])
        return tweetText

    


#keys needed to connect to Twitter API
consumerKey = "oHODtaZ4lhbBNzdipu264EZyB"
consumerSecret = "9FSSz45g79bIZ86tYtI1A16v2qefbxPDovxriDTftTxGScJkkM"
accessToken = "1580913027146194944-lJjqkVc7y7bvliIpcowcWYavTZxrBg"
accessSecret = "QTkLncj5RimG7oz7JgTlBavpHLn6Xh7Yw69BZLZQb6iFT"
bearerToken = "AAAAAAAAAAAAAAAAAAAAAOWqiAEAAAAAQNuCPNSbxjs2AGzGM%2FpS7qTNFUo%3D9S04BtXdeU4Pv2Ckyi3JW1dUzYUWJjl7Dg064yVrj9JG4e67oV"

#Authenticates user with Twitter API
client = tweepy.Client(bearerToken, consumerKey, consumerSecret, accessToken, accessSecret)