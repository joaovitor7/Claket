import json

import requests
import gmail_api
from flask import request

from backend.Tag import Tag
from backend.SentimentoPredominante import SentimentoPredominante
#from backend.coleta_tweets import *
from backend.classificador import *

def avaliar(jsonAvaliar):
    jsonObjects = json.loads(jsonAvaliar)
    roteiro_id = jsonObjects["roteiroId"]
    list_palavras = jsonObjects["palavras"]

    tags = []

    for jsonObject in list_palavras:
        texto = jsonObject['tag']
        sentimento = jsonObject['sentimento']
        qtTweets = jsonObject['quantidadeTweets']

        tag = Tag()
        tag.setTag(texto)
        tag.setSentimento(sentimento)
        tag.setQtTweets(qtTweets)

        tags.append(tag)


    for tag in tags:
        sentimento = tag.getSentimento()
        if sentimento == "null":
            texto = tag.getTag()
            sentimento, qtTweets = determinarSentimento(texto)
            tag.setSentimento(sentimento)
            tag.setQtTweets(qtTweets)

    nota = calculaNota(tags)

    #jsonTags = json.dumps([tag.to_json() for tag in tags])
    jsonTags = [tag.to_json() for tag in tags]
    jsonResponse = json.dumps({"tags": jsonTags, "nota": nota, "roteiroId":roteiro_id})
    #return jsonResponse
    print(jsonResponse, "oie")
    resposta = requests.post('https://646749e7.ngrok.io', data= jsonResponse, timeout = 10000)
    # print(str(resposta.json()))
    # print(jsonResponse)
    print("FINALIZADO")

def determinarSentimento(tag):
    tweets = coletar_tweets(tag, 10)
    qtTweets = len(tweets)

    contadorPositivo, contadorNegativo, contadorNeutro = contaTweetsClasse(tweets)

    sentimento = calcularPredominante(contadorPositivo, contadorNegativo, contadorNeutro)

    return sentimento, qtTweets

def calcularPredominante(numPositivo, numNegativo, numNeutro):

    positivo = SentimentoPredominante("positivo", numPositivo)
    negativo = SentimentoPredominante("negativo", numNegativo)
    neutro = SentimentoPredominante("neutro", numNeutro)

    if numPositivo == numNegativo:
        sentimento = neutro.getTexto()
        return sentimento


    if numPositivo > numNegativo:
        predominante = positivo
    else:
        predominante = negativo

    qtTweets = predominante.getQtTweets()

    if qtTweets >= numNeutro:
        sentimento = predominante.getTexto() #texto
    else:
        sentimento = neutro.getTexto()

    return sentimento

def contaTweetsClasse(tweets):

    contadorPositivo = 0
    contadorNegativo = 0
    contadorNeutro = 0

    for tweet in tweets:
        sentimento = classificar(tweet)
        if sentimento.lower() == "positivo":
            contadorPositivo += 1
        elif sentimento.lower() == "negativo":
            contadorNegativo += 1
        else:
            contadorNeutro += 1
    print("%d %d %d" % (contadorPositivo, contadorNegativo, contadorNeutro))
    return contadorPositivo, contadorNegativo, contadorNeutro

def calculaNota(listaTags):

    totalTweets = 0 # só para tags com sentimento positivo ou negativo
    for tag in listaTags:
        sentimento = tag.getSentimento().lower()
        print(sentimento)
        if sentimento != "neutro":
            qtTweets = tag.getQtTweets()
            print(qtTweets)
            totalTweets += qtTweets

    if totalTweets == 0:
        return 5

    pesoNota = 10.0/totalTweets
    notaFinal = 0

    for tag in listaTags:
        sentimento = tag.getSentimento().lower()
        if sentimento == "positivo":
            qtTweets = tag.getQtTweets()
            notaFinal += pesoNota * qtTweets

    notaFinal = round(notaFinal,2)
    return notaFinal
"""
tag1 = Tag("fantasma","null",100)
tag2 = Tag("palhaco", "null", 30)
tag3 = Tag("explosao", "null", 50)
tag4 = Tag("crianca", "null", 45)

tag5 = Tag("amor", "null", 98)
tag6 = Tag("casamento", "null", 44)
tag7 = Tag("bebida", "null", 1)
tag8 = Tag("sequestro", "null", 10)
tag9 = Tag("carro", "null", 122)
tag10 = Tag("caneta", "null", 73)


tags = [tag1,tag2,tag3,tag4]#,tag5, tag6,tag7,tag8,tag9,tag10]

jsonAvaliar = json.dumps([tag.to_json() for tag in tags])
print(jsonAvaliar)
print(type(jsonAvaliar))
#jsonResposta = avaliar(jsonAvaliar)
#print(jsonResposta)
"""
