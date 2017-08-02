from flask import Flask, request
from flask_restful import Resource, Api
import json

from backend.ControladorAvaliacao import avaliar

app = Flask(__name__)
api = Api(app)

class ClaketAPI(Resource):
    def get(self):
        jsons = request.get_data()
        json_decode = jsons.decode('utf-8')
        json_resposta = avaliar(json.dumps(json.loads(json_decode)))
        return json_resposta

api.add_resource(ClaketAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)