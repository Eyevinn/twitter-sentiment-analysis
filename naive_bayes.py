import math

class TextClassifier():
    def __init__(self, classes = ["s","a"]):
        self.classes = classes
        self.word_model = {}  # write code to dynamically create dictionary independant of number of classes
        self.class_count = {}
        for cl in classes:
            self.word_model[cl] = {}
            self.class_count[cl] = 0
        self.counter = {}

    def save_model(self, file_name = "model.txt"):
        file = open(file_name,"w")
        for cl in self.word_model:
            file.write("###:"+cl)
            for word in self.word_model[cl]:
                file.write("@@@:"+word+"---"+str(self.word_model[cl][word]))
    
        for cl in self.class_count:
            pass
        file.close()

    def load_model():
        pass

    def train(self, set_of_tweets):
        uniq_words = set()
        for tweet in set_of_tweets:
            if tweet.cl in self.word_model:
                if tweet.cl == self.classes[0]:
                    self.class_count[self.classes[0]] +=1
                elif tweet.cl == self.classes[1]:
                    self.class_count[self.classes[1]] +=1
                for word in tweet.tweet:
                    uniq_words.add(word)
                    if word in self.word_model[tweet.cl]:
                        self.word_model[tweet.cl][word] += 1
                    else:
                        self.word_model[tweet.cl][word] = 1
    
        for word in uniq_words: # make sure each word is represented at least once in every class.
            for c in self.class_count:
                if word not in self.word_model[c]:
                    self.word_model[c][word] = 1
                else:
                    self.word_model[c][word] += 1

        for i in self.classes: #total number of words in each class
            self.counter[i] = sum(self.word_model[i].values())
                    
        for i in self.classes: #convert each value in model to log of probability
            for word in self.word_model[i]:
                self.word_model[i][word] = math.log(float(self.word_model[i][word])/self.counter[i])
    
        total_count = sum(self.class_count.values()) #total number of words in model
        for i in self.class_count: #log of probability of each class
            self.class_count[i]= math.log(float(self.class_count[i])/total_count)

    def predict(self, tweet):
        class_prob = self.class_count
        for word in tweet:
            for cl in class_prob:
                class_prob[cl] += self.word_model[cl][word]
        probability = 0
        prediction = ""
        for i in class_prob:
            if -class_prob[i] > guess:
                probability = -class_prob[i]
                prediction = i
        return prediction







