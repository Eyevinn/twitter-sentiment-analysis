import re
from nltk.stem.wordnet import WordNetLemmatizer

stop_words = [""]

lemmatizer = WordNetLemmatizer()

def import_stop_words(file = "text_files/stop_words.txt"):
    file = open(file)
    for i in file:
        stop_words.append(i[0:-1]) #remove \n from each word

def process_word(word, signs_to_remove = ["@","#","!",","]):
    if word in stop_words:
        return "StopWords"
    if "https://t.co/" in word:
        return "RemovedLinks"
    if word == "but":
        print("but")
    for i in signs_to_remove:
        word = re.sub(i,"",word)
    word = word.lower()

    word = lemmatizer.lemmatize(word.decode('utf-8'))
    word = word.encode("utf-8")
    return word

def process_tweet(tweet):
    new_tweet = []
    for word in tweet:
        new_tweet.append(process_word(word))
    return new_tweet

def process_set_of_tweets(set_of_tweets):
    new_tweets = []
    for i in set_of_tweets:
        i.tweet = process_tweet(i.tweet)
        new_tweets.append(i)
    return new_tweets



import_stop_words()
