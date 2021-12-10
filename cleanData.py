import re
import pandas as pd
word_index_path ="indexed_words.csv"
word_index=pd.read_csv(word_index_path)
word_index=dict(zip(word_index.Words, word_index.Indexed))


def removePunctuation(text):
  for char in punctuation:
    text = text.replace(char, '')
  return text

def cleanTxt(text):
    text = str(text)
    text = re.sub(r'@[A-Za-z0-9]+', "", text) # removes mentions on tweets
    text = re.sub(r'#', "", text) # removes #tags on tweets'
    text = re.sub(r':', "", text) # removes #tags on tweets
    text = re.sub(r'RT[\s]+', "", text) # removes #tags on tweets
    text = re.sub(r'http\S+', '', text) # removes hypyer links
    text = removePunctuation(text)
    # text = removeLocalWords(text)
    # text = re.sub(r'http\S+', '', text) # removes hypyer links
    return text.strip().lower()


def review_encoder(text):
  arr=[word_index[word] for word in text]
  return arr

def pad_sequences(array):
    n = 30 - len(array)
    temp = [0] * n
    array.extend( temp)
    return array[:30]


def loadTweet(tweet):
    cleanTweets = []
    for word in tweet.split(" "):
        if word  in word_index.keys():
            cleanTweets.append(word)

    cleanTweets = review_encoder(cleanTweets)
    cleanTweets = pad_sequences(cleanTweets)
    return cleanTweets

