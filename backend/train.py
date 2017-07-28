import pickle
import csv
from textblob.classifiers import NaiveBayesClassifier

with open("new_sample.tsv", encoding="utf-8", newline='') as f:
    #dialeto = csv.Sniffer().sniff(f.read(1024), delimiters="\t")
    dialeto = csv.Sniffer().sniff(f.read(4096), delimiters='\t') # Coloquei 4096 bytes para ler
    f.seek(0)
    dado = csv.reader(f, dialeto)
    lista = []
    for l in dado:
        lista.append(tuple(l))
    cl = NaiveBayesClassifier(lista)
    g = open("trained.pickle", "wb")
    pickle.dump(cl, g)
    g.close()
