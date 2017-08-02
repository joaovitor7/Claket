import json
from Tag import Tag
from SentimentoPredominante import SentimentoPredominante
#from backend.coleta_tweets import *
from classificador import *

def avaliar(jsonAvaliar):
    jsonObjects = json.loads(jsonAvaliar)
    tags = []

    for jsonObject in jsonObjects:
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
    jsonResponse = json.dumps({"tags": jsonTags, "nota": nota})
    return jsonResponse

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

    totalTweets = 1 # só para tags com sentimento positivo ou negativo
    for tag in listaTags:
        sentimento = tag.getSentimento().lower()
        print(sentimento)
        if sentimento != "neutro":
            qtTweets = tag.getQtTweets()
            print(qtTweets)
            totalTweets += qtTweets

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