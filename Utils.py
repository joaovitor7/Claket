import json
import datetime

def juntarPalavras(palavras):
    palavrasChave = ""
    for palavraTemp in palavras:
        palavrasChave += palavraTemp.getTag() + ", "

    palavrasChave = palavrasChave[0:-2]
    return palavrasChave

def montarJson(palavrasChave):


    palavraChaveLista = []
    for palavraTemp in palavrasChave:
        dicionarioTemp = {}
        dicionarioTemp['tag'] = palavraTemp.getTag()
        dicionarioTemp['sentimento'] = palavraTemp.getSentimento()
        dicionarioTemp['quantidadeTweets'] = palavraTemp.getQntTweets()
        palavraChaveLista.append(dicionarioTemp)

    jsonRetorno = json.dumps(palavraChaveLista)
    return jsonRetorno

