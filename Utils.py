import json
import datetime

def juntarPalavras(palavras):
    palavrasChave = ""
    for palavraTemp in palavras:
        palavrasChave += palavraTemp.getTag() + ", "

    palavrasChave = palavrasChave[0:-2]
    return palavrasChave

def montarJson(palavrasChave, roteiroId):

    data = {}
    palavraChaveLista = []
    for palavraTemp in palavrasChave:
        dicionarioTemp = {}
        dicionarioTemp['tag'] = palavraTemp.getTag()
        dicionarioTemp['sentimento'] = palavraTemp.getSentimento()
        dicionarioTemp['quantidadeTweets'] = palavraTemp.getQntTweets()
        palavraChaveLista.append(dicionarioTemp)

    data['palavras'] = palavraChaveLista
    data['roteiroId'] = roteiroId


    jsonRetorno = json.dumps(data)
    return jsonRetorno