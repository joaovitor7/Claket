import datetime
import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

#f = open("tweets.csv", "w")

def main():

    def printTweet(descr, t):
        print(descr)
        print("Username: %s" % t.username)
        print("Retweets: %d" % t.retweets)
        print("Text: %s" % t.text)
        print("Mentions: %s" % t.mentions)
        print("Hashtags: %s" % t.hashtags)

# Exemplo de coleta de tweets do user 'peticormei' dentro da faixa de datas de 26/06/2017 a 29/06/2017, limitando a 20 tweets
#tweetCriteria = got.manager.TweetCriteria().setUsername("peticormei").setSince("2017-06-26").setUntil("2017-06-29").setMaxTweets(20)
#tweet = got.manager.TweetManager.getTweets(tweetCriteria)
#        for tw in tweet:
#	        printTweet("### Exemplo - Get tweets by username and bound dates [peticormei, '26/06/2017', '29/06/2017']", tw)

# Exemplo de coleta de tweets por palavra-chave, dentro de uma faixa de data
#    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('spiderman').setSince("2017-06-12").setUntil("2017-07-17").setMaxTweets(100)
#    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
#    for t in tweets:
#        printTweet("### Exemplo - Get tweets by subject and bound dates [lula]", t)
#        tweetString = [t.text, t.date.date().__str__()]
#        f.writelines('<>'.join(tweetString).encode("utf-8") + "\n")
#    f.close()

    def coletar_tweets(palavra, quant_tweets=100):
        data = datetime.datetime.now() - datetime.timedelta(30)
        dataHoje = datetime.datetime.now()
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(palavra).setSince(data.date().__str__()).setUntil(dataHoje.date().__str__()).setMaxTweets(100)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        return tweets

    def salvar_tweets(tweets):
        with open("tweets.csv", "w") as f:
            for t in tweets:
                tweetString = [t.text, t.date.date().__str__()]
                f.writelines('<>'.join(tweetString).encode("utf-8") + "\n")

    salvar_tweets(coletar_tweets("carros"))


if __name__ == '__main__':
    main()
