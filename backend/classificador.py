# -*- coding: utf-8 -*-
import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import pickle
import datetime

lista_filmes = [
    'mercenarios', 'velozes e furiosos', 'anabelle', 'invocacao do mal',
    'crepusculo', 'meu malvado favorito', 'querido john', 'homem aranha',
    'mulher maravilha', 'se beber nao case', 'defensores', 'o poderoso chefinho',
    'baywatch', 'meu passado me condena', 'american pie'
]

lista_filmes_2 = [
    'anabelle', 'homem aranha'
]

def classificar(texto):
    with open("trained.pickle", "rb") as f:
        cl = pickle.load(f)
        resultado = TextBlob(texto, classifier=cl)
        sentimento = resultado.classify()
        print(sentimento)
        return sentimento


def coletar_tweets(palavra, quant_tweets=10):
    lista_tweets = []
    for filme in lista_filmes_2:
        query = palavra + ' ' + filme
        data = datetime.datetime.now() - datetime.timedelta(30)
        dataHoje = datetime.datetime.now()
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query) \
            .setSince(data.date().__str__()).setUntil(dataHoje \
            .date().__str__()).setMaxTweets(quant_tweets)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        lista_tweets.append(tweets)
    lista_flat = flat_lista(lista_tweets)
    return lista_flat


def flat_lista(lista_de_listas):
    lista_retorno = []
    for lista in lista_de_listas:
        for tweet in lista:
            lista_retorno.append(tweet.text)
    return lista_retorno
