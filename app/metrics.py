from flask import jsonify
from flask_restful import Resource

class Health(Resource):
    def get(self):
        return {'status': 'ok'}

class Ready(Resource):
    def get(self):
        return {'status': 'ready'}