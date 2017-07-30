from random import randint



class PalavraChave():

	def __init__(self, id, tag, sentimento = 'null', qntTweets = 0):
		self.__id = id
		self.__tag = tag
		self.__sentimento = sentimento
		self.__qntTweets = qntTweets

	def getId(self):
		return self.__id
		
	def setId(id):
		self.__id = id

	def getTag(self):
		return self.__tag
		
	def setTag(tag):
		self.__tag = tag

	def getSentimento(self):
		return self.__sentimento
		
	def setSentimento(tag):
		self.__sentimento = sentimento

class Roteiro():

	def __init__(self, id, titulo, palavrasChaves, generos, aceitacao = None, dataAvaliacao = '1990/12/12'):
		self.__id = id
		self.__titulo = titulo
		self.__aceitacao = aceitacao
		self.__palavrasChaves = palavrasChaves
		self.__dataAvaliacao = dataAvaliacao
		self.__generos = generos

	def getId(self):
		return self.__id
		
	def setId(id):
		self.__id = id

	def getTitulo(self):
		return self.__titulo
		
	def setTitulo(titulo):
		self.__titulo = titulo

	def getAceitacao(self):
		return self.__aceitacao
		
	def setAceitacao(aceitacao):
		self.__aceitacao = aceitacao

	def getPalavrasChave(self):
		return self.__palavrasChaves
		
	def setPalavrasChave(palavrasChave):
		self.__palavrasChave = palavrasChave

	def getDataAvaliacao(self):
		return self.__dataAvaliacao
		
	def setDataAvaliacao(dataAvaliacao):
		self.__dataAvaliacao = dataAvaliacao

	def getGeneros(self):
		return self.__generos
		
	def setGeneros(generos):
		self.__generos = generos



class Usuario():

	def __init__(self, nome, email, senha, roteiros, cpf, plano, dataAquisicao):
		self.__cpf = cpf
		self.__nome = nome
		self.__email = email
		self.__senha = senha
		self.__roteiros = roteiros
		self.__plano = plano
		self.__dataAquisicao = dataAquisicao



	def getCpf(self):
		return self.__cpf
		
	def setCpf(cpf):
		self.__cpf = cpf

	def getNome(self):
		return self.__nome
		
	def setNome(nome):
		self.__nome = nome

	def getEmail(self):
		return self.__email
		
	def setEmail(email):
		self.__email = email

	def getSenha(self):
		return self.__senha
		
	def setSenha(senha):
		self.__senha = senha

	def getRoteiros(self):
		return self.__roteiros
		
	def setRoteiros(roteiros):
		self.__roteiros = roteiros

	def getPlano(self):
		return self.__planos
		
	def setPlano(planos):
		self.__planos = planos	

	def getDataAquisicao(self):
		return self.__dataAquisicao
		
	def setDataAquisicao(dataAquisicao):
		self.__dataAquisicao = dataAquisicao

class Plano():
	def __init__(self, id, preco, nome, imagem, qtdRoteiro):
		self.__id = id
		self.__preco = preco
		self.__nome = nome
		self.__imagem = imagem
		self.__qtdRoteiro = qtdRoteiro

	def getId(self):
		return self.__id
		
	def setId(id):
		self.__id = id

	def getPreco(self):
		return self.__preco
		
	def setPreco(preco):
		self.__preco = preco

	def getNome(self):
		return self.__nome
		
	def setNome(nome):
		self.__nome = nome

	def getImagem(self):
		return self.__imagem
		
	def setImagem(imagem):
		self.__imagem = imagem

	def getQtdRoteiro(self):
		return self.__qtdRoteiro
		
	def setQtdRoteiro(qtdRoteiro):
		self.__qtdRoteiro = qtdRoteiro


class UsuarioPlano():

	def __init__(self, id, qtdRoteiroAvaliados, dataAquisicao, usuario, plano):
		self.__id = id
		self.__qtdRoteiroAvaliados = qtdRoteiroAvaliados
		self.__dataAquisicao = dataAquisicao
		self.__usuario = usuario
		self.__plano = plano

	def getId(self):
		return self.__id
		
	def setId(id):
		self.__id = id

	def getQtdRoteirosAvaliados(self):
		return self.__qtdRoteirosAvaliados
		
	def setQtdRoteirosAvaliados(qtdRoteirosAvaliados):
		self.__qtdRoteirosAvaliados = qtdRoteirosAvaliados

	def getDataAquisicao(self):
		return self.__dataAquisicao
		
	def setDataAquisicao(dataAquisicao):
		self.__dataAquisicao = dataAquisicao

	def getUsuario(self):
		return self.__usuario
		
	def setUsuario(usuario):
		self.__usuario = usuario

	def getPlano(self):
		return self.__plano
		
	def setPlano(plano):
		self.__plano = plano
