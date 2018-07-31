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

# print(result)

# tb = TextBlob(result)
#
# filtered_words = [""]
#
# common_words = ["about", "when", "http"]
#
# for word in result:
#     if len(word) <= 3 or word in common_words:
#         filtered_words.append(word)
#         continue
#     # elif len(word) > 3:
#         # unfiltered_words.append(word)
#         # print(word)
#
# print(len(filtered_words))
# print(len(result))
