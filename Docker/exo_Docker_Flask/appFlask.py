from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

host = os.environ.get('MONGO_HOST', 'localhost')
port = int(os.environ.get('MONGO_PORT', 27017))

# Connexion à la base de données MongoDB
client = MongoClient(host=host, port=port)
db = client.Bdd_user
coll = db.user

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/create_user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    result = coll.insert_one(user_data)
    data['id'] = result.inserted_id
    return jsonify({'message': 'User created successfully', 'user_id': str(data['id'])})


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = coll.find_one({'_id': ObjectId(user_id)})
    user['_id'] = str(user['_id'])
    return jsonify({'user': user})


@app.route('/users', methods=['GET'])
def get_users():
    users = list(coll.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify({'users': users})  


@app.route('/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    user_data['_id'] = ObjectId(user_id)
    result = coll.replace_one({'_id': ObjectId(user_id)},user_data)
    user_data['_id'] = str(result.inserted_id)
    return jsonify({'message': 'User updated successfully'})


@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = coll.find_one({'_id': ObjectId(user_id)})
    result = coll.delete_one({'_id': ObjectId(user_id)})
    return jsonify({'message': 'User deleted successfully'})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
