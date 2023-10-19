from flask import jsonify, request
from flask_restful import Resource

# Define users list
users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'}
]

class Users(Resource):
    def get(self):
        # Return a list of all users
        return jsonify(users)

    def post(self):
        # Create a new user
        user = request.get_json()
        users.append(user)
        return jsonify(user)

class User(Resource):
    def get(self, user_id):
        for user in users:
            if user['id'] == user_id:
                return jsonify(user)
        return jsonify({'message': 'User not found'})

    def put(self, user_id):
        user = request.get_json()
        for i in range(len(users)):
            if users[i]['id'] == user_id:
                users[i] = user
                return jsonify(user)
        return jsonify({'message': 'User not found'})

    def delete(self, user_id):
        for i in range(len(users)):
            if users[i]['id'] == user_id:
                del users[i]
                return jsonify({'message': 'User deleted'})
        return jsonify({'message': 'User not found'})