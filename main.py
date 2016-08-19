
import classes
import lang_corr
from naive_bayes import TextClassifier
import classify
import search
import html_gen
import auth #keys = {'consumer_key':ckey, 'consumer_secret':csecret,
#'access_token_key':atoken, 'access_token_secret':asecret}

#init

def load_tweets(file):
    tweets = []
    file = open(file)
    for line in file:
        line = line.split("~")
        tweets.append(classes.TrainTweet(line[0],line[1]))
    tweets = lg_proccessor.process_set_of_tweets(tweets)
    return tweets



train_classifier = classify.Classifier()
lg_proccessor = lang_corr.LangProccessor()

#search.search(query = "@tv4")  #get tweets from twitter api
train_classifier.random_classification()   #randomly classify tweets. Test function
tweets = load_tweets("text_files/trained.txt")  # load classified tweets

cl = TextClassifier() #create classifier object
cl.train(tweets) # train on classified tweets

#print(cl.predict(["enjoy","enjoy","enjoy","enjoy","enjoy"]))

file = open("index.html","w") #open html file for writing

# create html file:
html_gen.insert_top(file)
html_gen.test(file, cl.word_model)
html_gen.insert_bottom(file)
file.close()
#cl.save_model()
#print(cl.word_model)
#print(cl.class_count)
#print(cl.counter)





