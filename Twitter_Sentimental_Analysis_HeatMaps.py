
# coding: utf-8

# In[ ]:


import tweepy 
import sys
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import csv

def percentage(part,whole):
    return 100*float(part)/float(whole)


#Credentials for Twitter App. Get Your from apps.twitter.com

consumerKey = 'OTlKyAAfuoi7fp5t58rXJDIgu'
consumerSecret = 'IG0RY9IXuX5ri7Joe9rw1enkguhTi0r6Tcts9mGQAm63j1dmT9'
accessToken = '1056748045822496768-fEcmLMea0KJDQOYUrihbHH7dxRA70E'
accessTokenSecret = 'Qu3x15KEgxIBz6iKJE7rlXiOolzdo1HaEGrKmz9H4wy7R'




#Establishing the connection

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm=input("Enter the keyword/Hashtag to search about :")
noofsearchTerms=int(input("Enter the no. of tweets to analyze :"))


ids=[]
Time=[]
Text=[]
Name=[]
Screen_name=[]
Location=[]
Friends_count=[]
Followers_count=[]



for tweet in tweepy.Cursor(api.search,q=searchTerm,lang="en",since="2015-01-01",result_type='popular').items(noofsearchTerms/2):
    ids.append(tweet.user.id)
    Time.append(tweet.created_at)
    Text.append(tweet.text)
    Name.append(tweet.user.name)
    Screen_name.append(tweet.user.screen_name)
    Location.append(tweet.user.location)
    Friends_count.append(tweet.user.friends_count)
    Followers_count.append(tweet.user.followers_count)
    
    
for tweet in tweepy.Cursor(api.search,q=searchTerm,lang="en",since="2015-01-01").items(noofsearchTerms/2):
    ids.append(tweet.user.id)
    Time.append(tweet.created_at)
    Text.append(tweet.text)
    Name.append(tweet.user.name)
    Screen_name.append(tweet.user.screen_name)
    Location.append(tweet.user.location)
    Friends_count.append(tweet.user.friends_count)
    Followers_count.append(tweet.user.followers_count)
    

d={
    'ids':ids,
    'Time':Time,
    'Text':Text,
    'Name':Name,
    'Screen_Name':Screen_name,
    'Location':Location,
    'Friends_count':Friends_count,
    'Followers_count':Followers_count
}

df=pd.DataFrame(d)


# In[ ]:


#Sorting Values By Followers Count to Find out the top Influencers who are INfluencing the topic

df.sort_values(by='Followers_count',inplace=True,ascending=False)
df['Sentiment']=0
noofTerms=df.shape[0]
df.head()


# In[ ]:


positive=0
negative=0
neutral=0
polarity=0

for i,tweet in enumerate(df['Text']):
    analysis=TextBlob(tweet)
    polarity+=analysis.sentiment.polarity
    if(analysis.sentiment.polarity==0.0):
        neutral+=1
    elif(analysis.sentiment.polarity>0.00):
        positive+=1
    elif(analysis.sentiment.polarity<0.00):
        negative+=1

    if(analysis.sentiment.polarity==0.0):
        df['Sentiment'][i]=1
    elif(analysis.sentiment.polarity>0.0):
        df['Sentiment'][i]=2
    elif(analysis.sentiment.polarity<0.0):
        df['Sentiment'][i]=0
        
        
#Calculating the percentage of all the positive,negative and neutral terms

positive=percentage(positive,noofTerms)
negative=percentage(negative,noofTerms)
neutral=percentage(neutral,noofTerms)


positive=format(positive, '.2f')
negative=format(negative, '.2f')
neutral=format(neutral, '.2f')



print("How people are reacting on "+ searchTerm +" by analyzing  "+" tweets.")


if (polarity==0):
    print("Overall Polarity is Neutral")
elif (polarity>0):
    print("Overall Polarity is Positive")
elif (polarity<0):
    print("Overall Polarity is Negative")
    



df.head()



#Visualization


labels=['Positive [' +str(positive)+'%]', 'Neutral [' +str(neutral)+'%]', 'Negative [' +str(negative)+'%]']
sizes=[positive,neutral,negative]
colors=['yellowgreen','gold','red']
patches,texts=plt.pie(sizes, colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("How people are reacting on "+ searchTerm +" by analyzing "+ str(noofsearchTerms)+" tweets.")
plt.axis("equal")
plt.tight_layout()
plt.show();


#Heat Map
import googlemaps
import gmplot

gmaps = googlemaps.Client(key='AIzaSyBNlCUex3Z4GcGNl-KU_35ccUPXmy0v5IM')
coordinates={'latitude':[],'longitude':[]}

for count,user_loc in enumerate(df['Location']):
    try:
        location=gmaps.geocode(user_loc)
        for i in location:
            coordinates['latitude'].append(i['geometry']['location']['lat'])
            coordinates['longitude'].append(i['geometry']['location']['lng'])
            
    except:
        pass

    
gmap = gmplot.GoogleMapPlotter(30, 0, 3)

gmap.heatmap(coordinates['latitude'],coordinates['longitude'],radius=20)
gmap.draw("python_heatmap.html")
df['SNo']=range(0,noofTerms)
df.reset_index(drop=True)
df.head()
df.index=df['SNo']

import googlemaps
import gmplot
df['Latitude']=0.000000
df['Longitude']=0.000000
gmaps = googlemaps.Client(key='AIzaSyBNlCUex3Z4GcGNl-KU_35ccUPXmy0v5IM')
lat=[]
lng=[]
for i,value in enumerate(df['Location']):
    try:
        location=gmaps.geocode(value)
        for j in location:
            df['Latitude'][i]=j['geometry']['location']['lat']
            df['Longitude'][i]=j['geometry']['location']['lng']
            
    except:
        pass
df.head()

import gmaps
import matplotlib.pyplot as plt 

gmaps.configure(api_key='AIzaSyBNlCUex3Z4GcGNl-KU_35ccUPXmy0v5IM')

negative_tweets= df[df['Sentiment'] == 0]
negative_tweets_location = negative_tweets[['Latitude', 'Longitude']]

neutral_tweets= df[df['Sentiment'] == 1]
neutral_tweets_location = neutral_tweets[['Latitude', 'Longitude']]

positive_tweets= df[df['Sentiment'] == 2]
positive_tweets_location = positive_tweets[['Latitude', 'Longitude']]


negative_layer = gmaps.symbol_layer(
    list(negative_tweets_location.values), fill_color='rgba(255, 0, 0, 0.8)',
    stroke_color='rgba(255, 0, 0, 0.8)', scale=5
)

neutral_layer = gmaps.symbol_layer(
    list(neutral_tweets_location.values), fill_color='rgba(250, 250, 210, 0.8)',
    stroke_color='rgba(255, 255, 102, 0.8)', scale=5
)
positive_layer = gmaps.symbol_layer(
    list(positive_tweets_location.values), fill_color='rgba(0, 100, 0, 0.8)',
    stroke_color='rgba(0, 100, 0, 0.8)', scale=5
)
#Green Color For POsitive tweets
#Red Color For Negative Tweets
#YelloW Color For Neutral Tweets

fig = gmaps.figure()
fig.add_layer(negative_layer)
fig.add_layer(neutral_layer)
fig.add_layer(positive_layer)
fig


# In[ ]:




