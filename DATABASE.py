from Claket import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class TabelaPlano(db.Model):
    __tablename__ = 'Plano'

    id= db.Column(db.INT(),primary_key=True, nullable=False)
    preco= db.Column(db.FLOAT(),nullable=False)
    nome= db.Column(db.VARCHAR(45),nullable=False)
    img= db.Column(db.VARCHAR(45), nullable=False)
    qtd_total_roteiros= db.Column(db.INT(), nullable=False)

    def __init__(self, id, preco, nome, img, qtd_total_roteiros):
        self.id= id
        self.preco=preco
        self.nome=nome
        self.img=img
        self.qtd_total_roteiros=qtd_total_roteiros



class TabelaUsuario(db.Model):
    __tablename__ = 'Usuario'

    cpf = db.Column(db.VARCHAR(45), primary_key=True, nullable=False)
    email = db.Column(db.VARCHAR(45), nullable=False)
    senha = db.Column(db.VARCHAR(45), nullable=False)
    nome = db.Column(db.VARCHAR(45), nullable=False)
    qtd_roteiros_avaliados=db.Column(db.INT())
    data_aquisicao_plano=db.Column(db.DATE(), nullable=False)
    id_plano=db.Column(db.INT(), ForeignKey('Plano.id'), nullable=False)

    fk_id_plano = relationship(TabelaPlano, foreign_keys=[id_plano])

    def __init__(self, cpf, email, senha, nome, qtd_roteiros_avaliados, qtd_total_roteiros, id_plano):
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.nome = nome
        self.qtd_roteiros_avaliados= qtd_roteiros_avaliados
        self.data_aquisicao_plano= data_aquisicao_plano
        self.id_plano= id_plano






class TabelaGenero(db.Model):
    __tablename__ = 'Genero'

    id = db.Column(db.INT(), primary_key=True)
    genero = db.Column(db.VARCHAR(45), nullable=False)

    def __init__(self, id, genero):
        self.id = id
        self.genero = genero


class TabelaPalavra_Chave(db.Model):
    __tablename__ = 'PalavraChave'

    id = db.Column(db.INT(), primary_key=True , nullable=False)
    palavra = db.Column(db.VARCHAR(45), nullable=False)

    def __init__(self, id, palavra):
        self.id = id
        self.palavra = palavra


class TabelaRoteiro(db.Model):
    __tablename__ = 'Roteiro'

    id = db.Column(db.INT(), primary_key=True)
    titulo = db.Column(db.VARCHAR(45), nullable=False)
    aceitacao = db.Column(db.VARCHAR(45), nullable=False)
    id_usuario = db.Column(db.VARCHAR(45), ForeignKey('Usuario.cpf'), nullable=False)
    data_avaliacao= db.Column(db.DATE(), nullable=False)

    id_Usuario_Roteiro = relationship(TabelaUsuario, foreign_keys=[id_usuario])

    def __init__(self, id, titulo, aceitacao, id_usuario, data_avaliacao):
        self.id = id
        self.titulo = titulo
        self.aceitacao = aceitacao
        self.id_usuario = id_usuario
        self.data_avaliacao = data_avaliacao



class TabelaRoteiro_Palavrachave(db.Model):
    __tablename__ = 'RoteiroPalavraChave'

    id_roteiro = db.Column(db.INT(), ForeignKey('Roteiro.id'), nullable=False, primary_key=True)
    id_palavra_chave = db.Column(db.INT(), ForeignKey('PalavraChave.id'), nullable=False, primary_key=True)

    id_Roteiro = relationship(TabelaRoteiro, foreign_keys=[id_roteiro])
    id_Palavra_Chave = relationship(TabelaPalavra_Chave, foreign_keys=[id_palavra_chave])

    def __init__(self, id_roteiro, id_palavra_chave):
        self.id_roteiro = id_roteiro
        self.id_palavra_chave = id_palavra_chave


class TabelaRoteiro_Genero(db.Model):
    __tablename__ = 'RoteiroGenero'

    id_roteiro = db.Column(db.INT(), ForeignKey('Roteiro.id'), nullable=False, primary_key=True)
    id_genero = db.Column(db.INT(), ForeignKey('Genero.id'), nullable=False, primary_key=True)

    id_Roteiro = relationship(TabelaRoteiro, foreign_keys=[id_roteiro])
    id_Genero = relationship(TabelaGenero, foreign_keys=[id_genero])

    def __init__(self, id_roteiro, id_genero):
        self.id_roteiro = id_roteiro
        self.id_genero = id_genero


class TabelaSentimento(db.Model):
    __tablename__ = 'Sentimento'

    id = db.Column(db.INT(), primary_key=True, nullable=False)
    sentimento = db.Column(db.VARCHAR(45), nullable=False)

    def __init__(self, id, sentimento):
        self.id = id
        self.sentimento = sentimento


class TabelaSentimento_Palavrachave(db.Model):
    __tablename__ = 'SentimentoPalavraChave'

    id_sentimento = db.Column(db.INT(), ForeignKey('Sentimento.id'), primary_key=True, nullable=False)
    id_palavrachave = db.Column(db.INT(), ForeignKey('PalavraChave.id'), primary_key=True, nullable=False)

    id_Sentimento = relationship(TabelaSentimento, foreign_keys=[id_sentimento])
    id_Palavrachave = relationship(TabelaPalavra_Chave, foreign_keys=[id_palavrachave])

    def __init__(self, id_sentimento, id_palavrachave):
        self.id_sentimento = id_sentimento
        self.id_palavrachave = id_palavrachave


class TabelaTweet(db.Model):
    __tablename__ = 'tweet'

    id = db.Column(db.INT(), primary_key=True, nullable=False)
    texto = db.Column(db.VARCHAR(200), nullable=False)
    data = db.Column(db.VARCHAR(45), nullable=False)
    id_sentimento = db.Column(db.INT(), ForeignKey('Sentimento.id'), nullable=False)


    fk_id_sentimento = relationship(TabelaSentimento, foreign_keys=[id_sentimento])

    def __init__(self, id, texto, data, sentimento):
        self.id = id
        self.texto = texto
        self.data = data
        self.sentimento= sentimento
        
"""
class TabelaTweet_Palavrachave(db.Model):
    __tablename__ = 'TweetPalavraChave'

    idtweet = db.Column(db.INT(), ForeignKey('Tweet.id'), nullable=False, primary_key=True)
    idpalavrachave = db.Column(db.INT(), ForeignKey('PalavraChave.id'), nullable=False, primary_key=True)

    id_Tweet = relationship(TabelaTweet, foreign_keys=[idtweet])
    id_Palavra_Chave = relationship(TabelaPalavra_Chave, foreign_keys=[idpalavrachave])

    def __init__(self, idtweet, idpalavrachave):
        self.idtweet = idtweet
        self.idpalavrachave = idpalavrachave
"""
