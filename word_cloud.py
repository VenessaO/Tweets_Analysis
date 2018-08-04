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
    break

result = ""

for word in tweets:
    result += str(word)

data = result.split()

words = []

for word in data:
    words.append(word)

print(words)

common_words = ["and", "or", "the", "is", "no", "a", "for", "yet", "so", "but", "be"]

for item in words:
    if item in common_words:
        words.remove(item)

print(words)
