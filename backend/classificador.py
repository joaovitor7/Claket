# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import pickle

def classificar(texto):

    with open("trained.pickle", "rb") as f:
        cl = pickle.load(f)
        resultado = TextBlob(texto, classifier=cl)
        sentimento = resultado.classify()
        return sentimento