import tweepy
import classes
import lang_corr
from naive_bayes import TextClassifier
import classify
import search
import html_gen
import auth #keys = {'consumer_key':ckey, 'consumer_secret':csecret,
#'access_token_key':atoken, 'access_token_secret':asecret}

#init
try:
    auth = tweepy.OAuthHandler(auth.keys['consumer_key'], auth.keys['consumer_secret'])
    api = tweepy.API(auth)
except:
    print("authorization failed.")


def load_tweets(file):
    tweets = []
    file = open(file)
    for line in file:
        line = line.split("~")
        tweets.append(classes.TrainTweet(line[0],line[1]))
    tweets = lang_corr.process_set_of_tweets(tweets)
    return tweets





#search.search("buffering")
classify.random_classification()
tweets = load_tweets("text_files/trained.txt")


cl = TextClassifier()
cl.train(tweets)

html_gen.insert_top(html_gen.file)
html_gen.test(html_gen.file, cl.model)
html_gen.insert_bottom(html_gen.file)


