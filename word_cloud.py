import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

tweets = []

for tweet in tweetData:
    tweets.append(tweet["text"])

total = concatenate(tweets)
