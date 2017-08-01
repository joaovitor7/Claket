import datetime
import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

FILE_NAME = "tweets_filmes_palavras.csv"

lista_palavras_old = [
    'zumbi', 'escuro', 'heroi', 'corrupcao', 'filme', 'explosao', 'acidente',
    'piratas', 'poder', 'espada', 'luta', 'medieval','vida', 'indie',
    'dinossauro','robo', 'espaco', 'animacao', 'chorei', 'sequestro'
]

lista_palavras = [
    'explosao', 'beijo', 'carro', 'susto', 'amor', 'heroi', 'romance', 'guerra',
    'emocionante', 'assalto', 'praia', 'equipe', 'luta', 'bebe', 'horrivel',
    'otimo', 'festa', 'adolescente', 'stifler', 'perigo', 'corrida', 'paciencia'
]


lista_filmes = [
    'mercenarios', 'velozes e furiosos', 'anabelle', 'invocacao do mal',
    'crepusculo', 'meu malvado favorito', 'querido john', 'homem aranha',
    'mulher maravilha', 'se beber nao case', 'defensores', 'o poderoso chefinho',
    'baywatch', 'meu passado me condena', 'american pie'
]


def coletar_tweets(palavra, quant_tweets=100):
    data = datetime.datetime.now() - datetime.timedelta(30)
    dataHoje = datetime.datetime.now()
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(palavra)\
                    .setSince(data.date().__str__()).setUntil(dataHoje\
                    .date().__str__()).setMaxTweets(quant_tweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    return tweets

def salvar_tweets(tweets, nome_arquivo):
    with open(nome_arquivo, "a") as f:
        for t in tweets:
            tweetString = [t.text, t.date.date().__str__()]
            f.writelines('\t'.join(tweetString).encode("utf-8") + "\n")

for palavra in lista_palavras:
    for filme in lista_filmes:
        query = palavra + ' ' + filme
        lista_tweets = coletar_tweets(query, 8)
        print (len(lista_tweets))
        print (query)
        salvar_tweets(lista_tweets, FILE_NAME)

