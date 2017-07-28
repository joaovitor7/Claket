class Tag():

    __tag = None
    __sentimento = None
    __qtTweets = None

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