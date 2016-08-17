






class TextClassifier():
    def __init__(self, classes = ["s","a"]):
        self.model = {classes[0]:{}, classes[1]:{}}

    def train(self, set_of_tweets):
        for tweet in set_of_tweets:
            if tweet.cl in self.model:
                for word in tweet.tweet:
                    if word in self.model[tweet.cl]:
                        #print("word in model")
                        self.model[tweet.cl][word] += 1
                    else:
                        self.model[tweet.cl][word] = 1

    def classify(tweets):
        pass

