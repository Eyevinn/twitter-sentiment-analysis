import sys
import random



def random_classification(file = "text_files/tweets.txt"):
    file = open(file)
    lista = []
    for line in file:
        assigned_class = random.choice(["a","s"])
        lista.append([line, str(assigned_class)])
    file.close()
    file = open("text_files/trained.txt", "w")
    for i in lista:
        file.write(str(i[0][0:-1])+"~"+ str(i[1])+"\n")
    file.close()



