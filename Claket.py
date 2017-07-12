from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/mydb'

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'

    cpf = db.Column(db.VARCHAR(45), primary_key=True, nullable=False)
    email = db.Column(db.VARCHAR(45), nullable=False)
    senha = db.Column(db.VARCHAR(45), nullable=False)
    nome = db.Column(db.VARCHAR(45), nullable=False)

    def __init__(self, cpf, email, senha, nome):
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.nome = nome



class Localidade(db.Model):
    __tablename__ = 'localidade'

    id = db.Column(db.INT(), primary_key=True)
    latitude = db.Column(db.VARCHAR(45), nullable=False)
    longitude = db.Column(db.VARCHAR(45), nullable=False)

    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude


class Palavra_Chave(db.Model):
    __tablename__ = 'palavra_chave'

    id = db.Column(db.INT(), primary_key=True)
    palavra = db.Column(db.VARCHAR(45), nullable=False)
    sentimento = db.Column(db.VARCHAR(45), nullable=False)

    def __init__(self, id, palavra, sentimento):
        self.id = id
        self.palavra = palavra
        self.sentimento = sentimento


class Roteiro(db.Model):
    __tablename__ = 'roteiro'

    id = db.Column(db.INT(), primary_key=True)
    titulo = db.Column(db.VARCHAR(45), nullable=False)
    aceitacao = db.Column(db.VARCHAR(45), nullable=False)
    idusuario = db.Column(db.VARCHAR(45), ForeignKey('usuario.cpf'), nullable=False)

    id_Usuario_Roteiro = relationship(Usuario, foreign_keys=[idusuario])

    def __init__(self, id, titulo, aceitacao, idusuario):
        self.id = id
        self.titulo = titulo
        self.aceitacao = aceitacao
        self.idusuario = idusuario


class Roteiro_Palavrachave(db.Model):
    __tablename__ = 'roteiro_palavrachave'

    idroteiro = db.Column(db.INT(), ForeignKey('roteiro.id'), nullable=False, primary_key=True)
    idpalavrachave = db.Column(db.INT(), ForeignKey('palavra_chave.id'), nullable=False, primary_key=True)

    id_Roteiro = relationship(Roteiro, foreign_keys=[idroteiro])
    id_Palavra_Chave = relationship(Palavra_Chave, foreign_keys=[idpalavrachave])

    def __init__(self, idroteiro, idpalavrachave):
        self.idroteiro = idroteiro
        self.idpalavrachave = idpalavrachave


class Sentimento(db.Model):
    __tablename__ = 'sentimento'

    id = db.Column(db.INT(), primary_key=True, nullable=False)
    sentimento = db.Column(db.VARCHAR(45), nullable=False)

    def __init__(self, id, sentimento):
        self.id = id
        self.sentimento = sentimento


class Tweet(db.Model):
    __tablename__ = 'tweet'

    id = db.Column(db.INT(), primary_key=True, nullable=False)
    texto = db.Column(db.VARCHAR(200), nullable=False)
    data = db.Column(db.VARCHAR(45), nullable=False)
    like = db.Column(db.INT(), nullable=False)
    idLocalidade = db.Column(db.INT(), ForeignKey('localidade.id'), nullable=False)

    id_Localidade = relationship(Localidade, foreign_keys=[idLocalidade])

    def __init__(self, id, texto, data, like, idLocalidade):
        self.id = id
        self.texto = texto
        self.data = data
        self.like = like
        self.idLocalidade = idLocalidade


class Tweet_Palavrachave(db.Model):
    __tablename__ = 'tweet_palavrachave'

    idtweet = db.Column(db.INT(), ForeignKey('tweet.id'), nullable=False, primary_key=True)
    idpalavrachave = db.Column(db.INT(), ForeignKey('palavra_chave.id'), nullable=False, primary_key=True)

    id_Tweet = relationship(Tweet, foreign_keys=[idtweet])
    id_Palavra_Chave = relationship(Palavra_Chave, foreign_keys=[idpalavrachave])

    def __init__(self, idtweet, idpalavrachave):
        self.idtweet = idtweet
        self.idpalavrachave = idpalavrachave


class Tweet_Sentimento(db.Model):
    __tablename__ = 'tweet_sentimento'

    idtweet = db.Column(db.INT(), ForeignKey('tweet.id'), nullable=False, primary_key=True)
    idsentimento = db.Column(db.INT(), ForeignKey('sentimento.id'), nullable=False, primary_key=True)

    id_Tweet = relationship(Tweet, foreign_keys=[idtweet])
    id_Sentimento = relationship(Sentimento, foreign_keys=[idsentimento])

    def __init__(self, idtweet, idsentimento):
        self.idtweet = idtweet
        self.idsentimento = idsentimento







@app.route('/')
def index():
    return 'Hello World'

@app.route("/cadastrarRoteiro")
def cadastrarRoteiro():
    return render_template("pages/forms.html")


@app.route("/cadastroRoteiro", methods=["GET", "POST"])
def cadastroRoteiro():
    if (request.method == "POST"):
        titulo = request.form.get("nome_roteiro")
        generos=['Acao','Drama', 'Aventura','Terror']
        palavras_chave= request.form.get("tokenfield")
        resultado=[]
        print(palavras_chave)
        for genero in generos:
            if request.form.get(genero)=='on':
                resultado.append(genero)

        palavras_chave=palavras_chave.split(", ")
        for palavra in palavras_chave:
            resultado.append(palavra)

        if (titulo and resultado and palavras_chave):
            r = Roteiro(id=None,titulo=titulo, aceitacao=0,idusuario=23456789)
            db.session.add(r)
            db.session.flush()
            for palavra in resultado:
                p=Palavra_Chave(id=None,palavra=palavra,sentimento='Neutro')
                db.session.add(p)
                db.session.flush()
                rp=Roteiro_Palavrachave(r.id,p.id)
                db.session.add(rp)
            db.session.commit()



        return ("Acho que não deu merda")
    return render_template("index.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0')
