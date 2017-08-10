from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/mydb'

api = Api(app)

db = SQLAlchemy(app)

from Controllers import *
from gmail_api import *

class ClientAPI(Resource):
    def post(self):
        jsons = request.get_data()
        json_decode = jsons.decode('utf-8')

	    resposta = json.loads(json_decode)

	    palavrasChaves = resposta['tags']


	    print(palavrasChaves)
	    for palavraTemp in palavrasChaves:
	        palavra = palavraTemp['tag']
	        sentimento = palavraTemp['sentimento']
	        quantidade_tweets = palavraTemp['quantidadeTweets']
	        palavraChave = PalavraChave(None,palavra,sentimento,quantidade_tweets)
	        PalavraChaveDAO.atualizarSentimento(palavraChave)


	    RoteiroDAO.setNota(roteiroId, resposta['nota'])

	    enviarEmail("silvaromerocf@gmail.com", "Wonder Woman", "çaca lá têu imêiu parssa tá no grau agora ;) e noiz")

        return json.dumps({ "status":"OK" })

api.add_resource(ClaketAPI, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')