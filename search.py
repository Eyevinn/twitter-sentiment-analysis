import tweepy
import sys
import lang_corr as lg
from main import auth, api

write = True


mode = "w"






def search(items=10, query = "query", language = "en",):
    index = 0
    if write:
        file = open("text_files/tweets.txt", mode)
    for tweet in tweepy.Cursor(api.search,q= query, rpp = 100, lang = language).items(100):
        if index == 100:
            break
        #combined search = [arg1, arg2]. Space = And. , = or
        #print tweet.text.lower()
        #print("#" * 25)
        if write:
            file.write(tweet.text.lower().encode("UTF-8") + "\n")
        index += 1
        #print(dir(tweet))




