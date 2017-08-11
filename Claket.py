import json
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/mydb'

api = Api(app)

db = SQLAlchemy(app)

from Controllers import *
from gmail_api import *
from Dominio import *
from DAO import *

class ClientAPI(Resource):
    def post(self):
        jsons = request.get_data()
        json_decode = jsons.decode('utf-8')
        resposta = json.loads(json_decode)

        #terminaAvaliacao(resposta)
        palavrasChaves = resposta['tags']

        print(palavrasChaves)

        for palavraTemp in palavrasChaves:
	        palavra = palavraTemp['tag']
	        sentimento = palavraTemp['sentimento']
	        quantidade_tweets = palavraTemp['quantidadeTweets']
	        palavraChave = PalavraChave(None,palavra,sentimento,quantidade_tweets)
	        PalavraChaveDAO.atualizarSentimento(palavraChave)

        RoteiroDAO.setNota(resposta['roteiroId'], resposta['nota'])

        roteiro = RoteiroDAO.getRoteiro(resposta['roteiroId'])

        enviarEmail("silvaromerocf@gmail.com", roteiro.getTitulo(), "çaca lá têu roteiro parssa tá no grau agora ;) e noiz")

        return json.dumps({ "status":"OK" })

api.add_resource(ClientAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)