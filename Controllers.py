from Claket import app
from DATABASE import *
from Dominio import *
from DAO import *
from flask import render_template, request, url_for, redirect


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/cadastrarRoteiro")
def cadastrarRoteiro():

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
            roteiro=Roteiro(titulo, resultado_palavrachave, resultado_genero)
            usuario=Usuario('nome','email','senha',[],'23456789', 1, '1990/12/12')

            #roteiroDAO=RoteiroDAO(roteiro,usuario)

            if RoteiroDAO.inserir(roteiro,usuario):
                return render_template("index.html")

    return render_template("index.html")


@app.route("/listagemRoteiro")
def listarRoteiros():
    roteiros = RoteiroDAO.listar('23456789')
    return render_template("roteiro/listagemRoteiro.html", roteiros=roteiros)

@app.route("/excluirRoteiro/<int:id>")
def excluirRoteiro(id):
    RoteiroDAO.excluir(id)
    return listarRoteiros()





@app.route("/formularioUsuario",)
def cadastroUsuario():
    return render_template('roteiro/formularioUsuario.html')


@app.route("/editarRoteiro/<string:id>", methods=["GET", "POST"])
def editarRoteiro(id):


    roteiro=RoteiroDAO.getRoteiro(id)

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

        roteiro = Roteiro(titulo, resultado_palavrachave, resultado_genero)


        RoteiroDAO.editar(id,roteiro)

        return listarRoteiros()


    elif (request.method == "GET"):


        def separarPalavras(palavras):

            palavrasChave=""
            for x in palavras:
                palavrasChave+=x+ ", "

            palavrasChave=palavrasChave[0:-2]
            return palavrasChave

        palavras=separarPalavras(roteiro.palavras_Chaves)

        totalGeneros=GeneroDAO.getGeneros()


        return render_template("roteiro/editarRoteiro.html", roteiro=roteiro,palavra_chave=palavras, totalGeneros=totalGeneros)
