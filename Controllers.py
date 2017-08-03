from Claket import app
from DATABASE import *
from Dominio import *
from Utils import *
from DAO import *
from flask import render_template, request, url_for, redirect
import json
import requests

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/planos')
def planos():
    return render_template("planos.html")

@app.route('/editarPlano', methods=["POST"])
def setPlanos():
    idPlano = request.form.get("plano")

    UsuarioDAO.setPlano('23456789', idPlano)
    return render_template("planos.html")

@app.route("/cadastrarRoteiro")
def cadastrarRoteiro():

    generos = GeneroDAO.getGeneros()
    return render_template("roteiro/formularioRoteiro.html", generos = generos)


@app.route("/cadastroRoteiro", methods=["POST"])
def cadastroRoteiro():
    if (request.method == "POST"):
        id=None
        titulo = request.form.get("nome_roteiro")
        generos = GeneroDAO.getGeneros()
        palavrasChave = request.form.get("tokenfield")
        resultadoGenero = []
        resultadoPalavraChave = []
        for generoTemp in generos:
            if request.form.get(generoTemp) == 'on':
                resultadoGenero.append(generoTemp)

        palavrasChave = palavrasChave.split(", ")
        for palavraTemp in palavrasChave:
            palavraChave = PalavraChave(id,palavraTemp)
            resultadoPalavraChave.append(palavraChave)


        roteiro=Roteiro(id,titulo, resultadoPalavraChave, resultadoGenero)
        usuario=Usuario('nome','email','senha',[],'23456789', 1, '1990/12/12')


        if RoteiroDAO.inserir(roteiro,usuario):
            return listarRoteiros()




@app.route("/listagemRoteiro")
def listarRoteiros():
    roteiros = RoteiroDAO.listar('23456789')
    return render_template("roteiro/listagemRoteiro.html", roteiros=roteiros)

@app.route("/excluirRoteiro/<int:idRoteiro>", methods=["GET"])
def excluirRoteiro(idRoteiro):

    # jsonData = request.get_json(force=True, silent=False, cache=True)
    # print(jsonData['idRoteiro'])

    # idRoteiro = jsonData['idRoteiro']
    
    RoteiroDAO.excluir(idRoteiro)

    return redirect(url_for('listarRoteiros'))


@app.route("/formularioUsuario")
def cadastroUsuario():

    return render_template('roteiro/formularioUsuario.html')


@app.route("/editarRoteiro/<string:id>", methods=["GET"])
def editarRoteiro(id):

    roteiro=RoteiroDAO.getRoteiro(id)

    palavras = juntarPalavras(roteiro.getPalavrasChave())

    totalGeneros = GeneroDAO.getGeneros()


    return render_template("roteiro/editarRoteiro.html", roteiro = roteiro ,palavra_chave = palavras, totalGeneros = totalGeneros)



@app.route("/editarRoteiroPost", methods=["POST"])
def editarRoteiroPost():

    print(request.form.get("idRoteiro"))

    idRoteiro = request.form.get("idRoteiro")

    roteiro = RoteiroDAO.getRoteiro(idRoteiro)

    titulo = request.form.get("nome_roteiro")

    generos = GeneroDAO.getGeneros()


    palavrasChave = request.form.get("tokenfield")
    resultadoGenero = []
    resultadoPalavraChave = []
    for generoTemp in generos:
        if request.form.get(generoTemp) == 'on':
            resultadoGenero.append(generoTemp)

    palavras_chave = palavrasChave.split(", ")

    for palavraTemp in palavras_chave:
        palavraChave = PalavraChave(idRoteiro, palavraTemp)
        resultadoPalavraChave.append(palavraChave)

    roteiro = Roteiro(idRoteiro,titulo, resultadoPalavraChave, resultadoGenero)


    RoteiroDAO.editar(roteiro)

    # return redirect(url_for('listarRoteiros'))
    return listarRoteiros()


@app.route("/detalharRoteiro/<int:id>")
def detalharRoteiro(id):
    roteiro = RoteiroDAO.getRoteiro(id)

    palavrasChaves = juntarPalavras(roteiro.getPalavrasChave())
    return render_template("roteiro/detalharRoteiro.html", roteiro = roteiro)

@app.route("/avaliar", methods=["POST"])
def avaliar():

    roteiroId = request.form.get('roteiroId')

    roteiro = RoteiroDAO.getRoteiro(roteiroId)

    palavrasChaves = roteiro.getPalavrasChave()

    jsonRetorno = montarJson(palavrasChaves)


    r = requests.get('https://8588f3b4.ngrok.io/', data= jsonRetorno, timeout = 10000)


    resposta1 = str(r.json())

    resposta = json.loads(resposta1)

    palavrasChaves = resposta['tags']


    print(palavrasChaves)
    for palavraTemp in palavrasChaves:
        palavra = palavraTemp['tag']
        sentimento = palavraTemp['sentimento']
        quantidade_tweets = palavraTemp['quantidadeTweets']
        palavraChave = PalavraChave(None,palavra,sentimento,quantidade_tweets)
        PalavraChaveDAO.atualizarSentimento(palavraChave)



    RoteiroDAO.setNota(roteiroId, resposta['nota'])

    return render_template('roteiro/listagemRoteiro.html')

@app.route("/json", methods=["GET"])
def testeJson():
    x = json.dumps({'teste':'olá mundo!'})
    return x