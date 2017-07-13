from Claket import app
from Models import *

from flask import render_template, request


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/cadastrarRoteiro")
def cadastrarRoteiro():
    # return render_template("roteiro/listagemRoteiro.html", myContent = open("templates/roteiro/cadastrarContent.html", 'r').read())
    return render_template("roteiro/formularioRoteiro.html")


@app.route("/cadastroRoteiro", methods=["GET", "POST"])
def cadastroRoteiro():
    if (request.method == "POST"):
        titulo = request.form.get("nome_roteiro")
        generos=['Acao','Drama', 'Aventura','Terror']
        palavras_chave= request.form.get("tokenfield")
        resultado=[]
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
                palavra_no_banco = Palavra_Chave.query.filter_by(palavra=palavra).first()
                if (palavra_no_banco == None):
                    p=Palavra_Chave(id=None,palavra=palavra,sentimento='Neutro')
                    db.session.add(p)
                    db.session.flush()
                    rp=Roteiro_Palavrachave(r.id,p.id)
                    db.session.add(rp)
                else:
                    rp = Roteiro_Palavrachave(r.id, palavra_no_banco.id)
                    db.session.add(rp)
            db.session.commit()

        return render_template("index.html")
    return render_template("index.html")

@app.route("/listagemRoteiro")
def listarRoteiros():
    return render_template("roteiro/listagemRoteiro.html")