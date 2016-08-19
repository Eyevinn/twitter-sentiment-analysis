import re
from nltk.stem.wordnet import WordNetLemmatizer

class LangProccessor(object):
    def __init__(self):
        self.stop_words = self.import_stop_words()
        self.lemmatizer = WordNetLemmatizer()
        self.unwanted_signs = ["\W","\d"]

    def import_stop_words(self,file = "text_files/stop_words.txt"):
        stop_words = []
        file = open(file)
        for i in file:
            stop_words.append(i[0:-1])
        return stop_words

    def remove_stop_words(self, word):
        if word in self.stop_words:
            return "StopWords"
        else:
            return word
    def remove_links(self, word):
        if "https://t.co/" in word:
            return "RemovedLinks"
        else:
            return word
    def remove_unwanted_signs(self,word):
        for i in self.unwanted_signs:
            word = re.sub(i,"",word)
        return word
    def remove_empty(self,word):
        if word == "":
            return "Empty"
        else:
            return word

    def process_word(self, word):
        word = self.remove_stop_words(word)
        word = self.remove_links(word)
        word = self.remove_unwanted_signs(word)
        word = self.remove_empty(word)
        word = word.lower() #lowercase word
        word = self.lemmatizer.lemmatize(word.decode('utf-8')) #lemmatize word
        word = word.encode("utf-8")
        return word

    def process_tweet(self, tweet):
        new_tweet = []
        for word in tweet:
            new_tweet.append(self.process_word(word))
        return new_tweet

    def process_set_of_tweets(self, set_of_tweets):
        new_tweets = []
        for i in set_of_tweets:
            i.tweet = self.process_tweet(i.tweet)
            new_tweets.append(i)
        return new_tweets



