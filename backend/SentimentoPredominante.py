class SentimentoPredominante():

    __texto = None
    __qtTweets = None

    def __init__(self, texto, qtTweets):
        self.__texto = texto
        self.__qtTweets = qtTweets

    def getTexto(self):
        return self.__texto

    def setTexto(self, texto):
        self.__texto = texto

    def getQtTweets(self):
        return self.__qtTweets

    def setQtTweets(self,qtTweets):
        self.__qtTweets = qtTweets