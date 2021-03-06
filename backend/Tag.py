import json

class Tag():

    __tag = None
    __sentimento = None
    __qtTweets = None

    def __init__(self, tag=None, sentimento=None, qtTweets=None):
        self.__tag = tag
        self.__sentimento = sentimento
        self.__qtTweets = qtTweets

    def getTag(self):
        return self.__tag

    def setTag(self,tag):
        self.__tag = tag

    def getSentimento(self):
        return self.__sentimento

    def setSentimento(self, sentimento):
        self.__sentimento = sentimento

    def getQtTweets(self):
        return self.__qtTweets

    def setQtTweets(self,qtTweets):
        self.__qtTweets = qtTweets

    def to_json(self):
        jsonObject = {"tag": self.getTag(),
               "sentimento": self.getSentimento(),
                "quantidadeTweets": self.getQtTweets()}
        return jsonObject

