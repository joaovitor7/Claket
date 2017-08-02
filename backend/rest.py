from flask import Flask, request
from flask_restful import Resource, Api
import json

from backend.ControladorAvaliacao import avaliar

app = Flask(__name__)
api = Api(app)

class ClaketAPI(Resource):
    def post(self):
        jsons = request.get_json()
        lista_jsons = []
        lista_jsons.append(jsons)
        json_resposta = avaliar(json.dumps(lista_jsons))
        return json_resposta

api.add_resource(ClaketAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)