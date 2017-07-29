import json
from backend.Tag import Tag
from backend.SentimentoPredominante import SentimentoPredominante
#from backend.coleta_tweets import *
#from backend.classificador import *

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

    jsonTags = json.dumps([tag.to_json() for tag in tags])

    jsonResponse = json.dumps({"tags": jsonTags, "nota": nota})

    return jsonResponse

def determinarSentimento(tag):
    tweets = coletar_tweets(tag)
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
        if sentimento == "positivo":
            contadorPositivo += 1
        elif sentimento == "negativo":
            contadorNegativo += 1
        else:
            contadorNeutro += 1

    return contadorPositivo, contadorNegativo, contadorNeutro

def calculaNota(listaTags):

    totalTweets = 0 # só para tags com sentimento positivo ou negativo
    for tag in listaTags:
        sentimento = tag.getSentimento().lower()
        if sentimento != "neutro":
            qtTweets = tag.getQtTweets()
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

tag1 = Tag("fantasma","positivo",100)
tag2 = Tag("palhaco", "positivo", 30)
tag3 = Tag("explosao", "positivo", 50)
tag4 = Tag("crianca", "neutro", 45)
tag5 = Tag("amor", "neutro", 98)
tag6 = Tag("casamento", "negativo", 44)
tag7 = Tag("bebida", "negativo", 1)
tag8 = Tag("sequestro", "neutro", 10)
tag9 = Tag("carro", "neutro", 122)
tag10 = Tag("caneta", "neutro", 73)


tags = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]

jsonAvaliar = json.dumps([tag.to_json() for tag in tags])

jsonResposta = avaliar(jsonAvaliar)
print(jsonResposta)