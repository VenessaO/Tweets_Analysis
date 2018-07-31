'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Continue your program below!
#json object or tweets are stored in tweetData

#iterate list of tweest_small
    # for each tweet access the text. Use the text feild tweet.text
    # print polarity

for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    print(tb.polarity)
    if tb.polarity > 0:
        print("positive")
    elif tb.polarity == 0:
        print("neutral")
    elif tb.polarity < 0:
        print("negative")
