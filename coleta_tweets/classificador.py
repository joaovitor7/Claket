# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import csv
import pickle

with open("tweets_filmes_palavras.tsv", encoding="utf-8", newline='') as f:
    dialeto = csv.Sniffer().sniff(f.read(1024), delimiters="\t")
    f.seek(0)
    dado = csv.reader(f, dialeto)
    lista = []
    for l in dado:
        lista.append(tuple(l))
    cl = NaiveBayesClassifier(lista)
    resultado = TextBlob("corrupcao deve ser combatida", classifier=cl)
    resultado2 = TextBlob("corrupcao esta alta no pais", classifier=cl)
    resultado3 = TextBlob("hoje vou a um casamento", classifier=cl)
    resultado4 = TextBlob("apocalipse zumbi", classifier=cl)
    print(resultado.classify())
    print(resultado2.classify())
    print(resultado3.classify())
    print(resultado4.classify())

"""
with open("trained.pickle", "rb") as f:
    cl = pickle.load(f)
    while True:
        query = input("Digite as palavras: ")
        resultado = TextBlob(query, classifier=cl)
        print(resultado.classify())

"""
"""
with open("trained.pickle", "rb") as f:
    cl = pickle.load(f)
    resultado = TextBlob("corrupcao deve ser combatida", classifier=cl)
    resultado2 = TextBlob("corrupcao esta alta no pais", classifier=cl)
    resultado3 = TextBlob("hoje vou a um casamento", classifier=cl)
    resultado4 = TextBlob("auto-escola", classifier=cl)
    print(resultado.classify())
    print(resultado2.classify())
    print(resultado3.classify())
    print(resultado4.classify())
"""
