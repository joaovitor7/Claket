import json

from flask import Flask, request
from flask_restful import Resource, Api
from threading import Thread

from backend.ControladorAvaliacao import avaliar

app = Flask(__name__)
api = Api(app)
thread = None

class ClaketAPI(Resource):
    def get(self):
        jsons = request.get_data()
        json_decode = jsons.decode('utf-8')
        thread = Thread(target=avaliar,  args=json.dumps(json.loads(json_decode)))
        thread.start()
        json_resposta = json.dumps({ "status":"OK" })
        return json_resposta

api.add_resource(ClaketAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)
