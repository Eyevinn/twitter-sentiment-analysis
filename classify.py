import sys
import random

class Classifier(object):
    def __init__(self, classes = ["a","s"]):
        self.classes = classes
    
    def random_classification(self,file = "text_files/tweets.txt"):
        file = open(file)
        lista = []
        for line in file:
            assigned_class = random.choice(self.classes)
            lista.append([line, str(assigned_class)])
        file.close()
        file = open("text_files/trained.txt", "w")
        for i in lista:
            file.write(str(i[0][0:-1])+"~"+ str(i[1])+"\n")
        file.close()



