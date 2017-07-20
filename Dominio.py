
class Palavra_Chave():

	def __init__(self, tag,sentimento='neutro'):
		self.tag=tag
		self.sentimento = sentimento

class Roteiro():

	def __init__(self,titulo, palavras_Chaves, generos, aceitacao='0', data_da_avaliacao='1990/12/12'):
		self.titulo = titulo
		self.aceitacao = aceitacao
		self.palavras_Chaves = palavras_Chaves
		self.data_da_avaliacao = data_da_avaliacao
		self.generos = generos

class Usuario():

	def __init__(self,nome,email,senha,roteiros,cpf,plano, data_de_aquisicao):
		self.cpf=cpf
		self.nome = nome
		self.email = email
		self.senha = senha
		self.roteiros = roteiros
		self.plano=plano
		self.data_de_aquisicao=data_de_aquisicao

class Plano():
	def __init__(self,preco, nome, imagem, qnt_roteiro):
		self.preco = preco
		self.nome = nome
		self.imagem = imagem
		self.qnt_roteiro = qnt_roteiro



class UsuarioPlano():

	def __init__(self, qnt_roteiros_avaliados,data_de_aquisicao,usuario,plano):
		self.qnt_roteiro = qnt_roteiro
		self.data_de_aquisicao = data_de_aquisicao
		self.usuario = usuario
		self.plano = plano
