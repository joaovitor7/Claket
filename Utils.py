def juntarPalavras(palavras):
    palavrasChave = ""
    for palavraTemp in palavras:
        palavrasChave += palavraTemp.getTag() + ", "

    palavrasChave = palavrasChave[0:-2]
    return palavrasChave