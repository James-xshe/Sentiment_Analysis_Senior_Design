# coding: utf-8

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import csv
import ui_v2
import pandas as pd

tweets = []


class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'OTlKyAAfuoi7fp5t58rXJDIgu'
        consumer_secret = 'IG0RY9IXuX5ri7Joe9rw1enkguhTi0r6Tcts9mGQAm63j1dmT9'
        access_token = '1056748045822496768-fEcmLMea0KJDQOYUrihbHH7dxRA70E'
        access_token_secret = 'Qu3x15KEgxIBz6iKJE7rlXiOolzdo1HaEGrKmz9H4wy7R'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set five categories of sentiment
        if 0.5 < analysis.sentiment.polarity <= 1:
            return 'strongly positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        elif 0 < analysis.sentiment.polarity < 0.5:
            return 'positive'
        elif -0.5 <= analysis.sentiment.polarity < 0:
            return 'negative'
        else:
            return 'strongly negative'

    def get_tweets(self, query, count=10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        global tweets

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count,lang='en',tweet_mode="extended")

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.full_text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.full_text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

                    # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def searchtweets(query_str):
    # creating object of TwitterClient class
    api = TwitterClient()
    # getting global variable
    global tweets
    # calling function to get tweets
   # tweets = api.get_tweets(query=query_str, count=1000)
    tweets = api.get_tweets(query=query_str, count=1000)

def stronglypos_per():
    global tweets
    sptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'strongly positive']
    # percentage of strongly positive tweets
    sptweets_per = 100 * len(sptweets) / len(tweets)
    return sptweets_per

def posper():
    global tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of  positive tweets
    ptweets_per = 100 * len(ptweets) / len(tweets)
    return ptweets_per

def negper():
    global tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of  negative tweets
    ntweets_per = 100 * len(ntweets) / len(tweets)
    return ntweets_per

def stronglyneg_per():
    global tweets
    sntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'strongly negative']
    # percentage of  strongly negative tweets
    sntweets_per = 100 * len(sntweets) / len(tweets)
    return sntweets_per

def neu_per():
    global tweets
    neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    # percentage of  neutral tweets
    neutweets_per = 100 * len(neutweets) / len(tweets)
    return neutweets_per

def stronglypos():
    # picking strongly positive tweets from tweets
    global tweets
    sptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'strongly positive']
    # percentage of strongly positive tweets
    sptweets_per = 100*len(sptweets)/len(tweets)
    print(sptweets_per)
    print("Strongly Positive tweets percentage: {} %".format(100 * len(sptweets) / len(tweets)))
    if sptweets:
        # writing strongly positive tweets into a txt file for word cloud
        # with open('stronglypos.txt', 'w') as f:
        #     for tweet in sptweets:
        #         f.write("%s\n" % tweet['text'])
        # with open('stronglypos', 'w', newline='') as myfile:
        #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        #     wr.writerow(sptweets)
        df = pd.DataFrame(sptweets, columns=['column'])
        df.to_csv('sptweets.csv', index=False, encoding='utf-8')

        # picking strongly positive tweets from tweets
        for tweet in sptweets[:15]:
            tweet['text']
        return tweet["text"]
    else:
        list = ['NULL']
        return list

def pos():
    # picking positive tweets from tweets
    global tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    if ptweets:
    # writing positive tweets into a txt file for word cloud
    # with open('pos.txt', 'w') as f:
    #     for tweet in ptweets:
    #         f.write("%s\n" % tweet['text'])
    #     with open('pos', 'w', newline='') as myfile:
    #         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #         wr.writerow(ptweets)
            df = pd.DataFrame(ptweets, columns=['column'])
            df.to_csv('ptweets.csv', index=False, encoding='utf-8')

    # picking positive tweets from tweets
            for tweet in ptweets[:15]:
                 tweet['text']
            return tweet['text']
    else:
        list = ['NULL']
        return list


def neg():
    # picking negative tweets from tweets
    global tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of positive tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    if ntweets:
    # writing negative tweets into a txt file for word cloud
    # with open('neg.txt', 'w') as f:
    #     for tweet in ntweets:
    #         f.write("%s\n" % tweet['text'])
    #     with open('neg', 'w', newline='') as myfile:
    #         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #         wr.writerow(ntweets)
        df = pd.DataFrame(ntweets, columns=['column'])
        df.to_csv('ntweets.csv', index=False, encoding='utf-8')

    # picking positive tweets from tweets
        for tweet in ntweets[:15]:
            tweet['text']
        return tweet["text"]
    else:
        list = ['NULL']
        return list

def stronglyneg():
    # picking positive tweets from tweets
    global tweets
    sntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'strongly negative']
    # percentage of strongly negative tweets
    print("Strongly negative tweets percentage: {} %".format(100 * len(sntweets) / len(tweets)))
    if sntweets:
        # writing strongly negative tweets into a txt file for word cloud
        # with open('stronglyneg.txt', 'w') as f:
        #     for tweet in sntweets:
        #         f.write("%s\n" % tweet['text'])
        # with open('stronglyneg', 'w', newline='') as myfile:
        #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        #     wr.writerow(sntweets)
        df = pd.DataFrame(sntweets,columns=['column'])
        df.to_csv('sntweets.csv', index=False, encoding='utf-8')
        # picking strongly negative tweets from tweets
        for tweet in sntweets[:15]:
            tweet['text']
        return tweet['text']
    else:
        list = ['NULL']
        return list[0]



#      return flag
# else:
# print(tweet['text'])

def neu():
    # picking negative tweets from tweets
    global tweets
    neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} %".format(100 * len(neutweets) / len(tweets)))
    # writing neutral tweets into a txt file for word cloud
    # with open('neu.txt', 'w') as f:
    #     for tweet in neutweets:
    #         f.write("%s\n" % tweet['text'])
    # with open('neu', 'w', newline='') as myfile:
    #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #     wr.writerow(neutweets)
    df = pd.DataFrame(neutweets, columns=['column'])
    df.to_csv('neutweets.csv', index=False, encoding='utf-8')

    # picking neutral tweets from tweets
    for tweet in neutweets[:15]:
        tweet['text']
    return tweet["text"]

    # printing first 5 positive tweets


#    print("\n\nPositive tweets:")
#    for tweet in ptweets[:15]:
#        print(tweet['text'])

# printing first 5 negative tweets
#   print("\n\nNegative tweets:")
#   for tweet in ntweets[:15]:
#       print(tweet['text'])
'''
if __name__ == "__main__": 
    # calling main function 
    main() 
'''
#
# searchtweets('huawei')
# stronglypos()
# pos()
# neg()
# neu()
# stronglyneg()
