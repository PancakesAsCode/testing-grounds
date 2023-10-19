from flask import jsonify
from flask_restful import Resource

class Hit(Resource):
    def get(self):
        return jsonify({'message': 'hello api'})