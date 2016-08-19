import tweepy
import sys
import lang_corr as lg
import auth

write = True
mode = "w"

def search(items=10, query = "test", language = "sv", file = "text_files/tweets.txt", amount = 1000):
    index = 0
    if write:
        file = open(file, mode)
    for tweet in tweepy.Cursor(auth.api.search,q= query, rpp = 100, lang = language).items(1000):
        if index == amount: # break loop when amount is reached. Tweepy seems unreliable.
            break
        if write:
            file.write(tweet.text.lower().encode("UTF-8") + "\n")
        index += 1





