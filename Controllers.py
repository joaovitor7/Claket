from Claket import app
from Models import *

from flask import render_template, request, url_for, redirect


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
        generos = ['Acao', 'Drama', 'Aventura', 'Terror']
        palavras_chave = request.form.get("tokenfield")
        resultado_genero = []
        resultado_palavrachave = []
        for genero in generos:
            if request.form.get(genero) == 'on':
                resultado_genero.append(genero)

        palavras_chave = palavras_chave.split(", ")
        for palavra in palavras_chave:
            resultado_palavrachave.append(palavra)

        if (titulo and resultado_genero and resultado_palavrachave and palavras_chave):
            r = Roteiro(id=None, titulo=titulo, aceitacao=0, idusuario=23456789)
            db.session.add(r)
            db.session.flush()
            for palavra in resultado_palavrachave:
                palavra_no_banco = Palavra_Chave.query.filter_by(palavra=palavra).first()
                if (palavra_no_banco == None):
                    p = Palavra_Chave(id=None, palavra=palavra)
                    db.session.add(p)
                    db.session.flush()
                    rp = Roteiro_Palavrachave(r.id, p.id)
                    db.session.add(rp)
                else:
                    rp = Roteiro_Palavrachave(r.id, palavra_no_banco.id)
                    db.session.add(rp)
            for genero in resultado_genero:
                genero_no_banco = Genero.query.filter_by(genero=genero).first()
                if genero_no_banco is None:
                    g = Genero(id=None, genero=genero)
                    db.session.add(g)
                    db.session.flush()
                    rg = Roteiro_Genero(r.id, g.id)
                    db.session.add(rg)
                else:
                    rg = Roteiro_Genero(r.id, genero_no_banco.id)
                    db.session.add(rg)
            db.session.commit()

        return render_template("index.html")
    return render_template("index.html")


@app.route("/listagemRoteiro")
def listarRoteiros():
    roteiros= Roteiro.query.filter_by(idusuario='23456789').all()
    return render_template("roteiro/listagemRoteiro.html", roteiros=roteiros)

@app.route("/excluirRoteiro/<int:id>")
def excluirRoteiro(id):
    roteiro= Roteiro.query.filter_by(id=id).first()
    db.session.delete(roteiro)
    db.session.commit()

    return listarRoteiros()

@app.route("/editarRoteiro/<int:id>", methods=["GET", "POST"])
def editarRoteiro(id):
    roteiro = Roteiro.query.filter_by(id=id).first()
    roteiro_palavrachave=Roteiro_Palavrachave.query.filter_by(idroteiro=id).all()
    roteiro_genero=Roteiro_Genero.filter_by(idroteiro=id).all()

    return roteiro_genero

@app.route("/formularioUsuario",)
def cadastroUsuario():
    return render_template('roteiro/formularioUsuario.html')