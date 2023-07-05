from flask import Flask, request, jsonify
from pymongo import MongoClient

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client[Bdd_user]  
collection = db[users] 

app = Flask(__name__)

# Route pour créer un nouvel élément
@app.route('/user', methods=['POST'])
def create_user():
    user = request.get_json()
    collection.insert_one(user)
    return jsonify({'message': 'Nouveau USER créé avec succès'})

# Route pour récupérer tous les éléments
@app.route('/users', methods=['GET'])
def get_all_users():
    users = list(collection.find())
    return jsonify(users)

# Route pour récupérer un élément par son ID
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    return jsonify(user)

# Route pour mettre à jour un élément
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    new_user = request.get_json()
    collection.update_one({'_id': ObjectId(user_id)}, {'$set': new_user})
    return jsonify({'message': 'USER mis à jour avec succès'})

# Route pour supprimer un élément
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    collection.delete_one({'_id': ObjectId(user_id)})
    return jsonify({'message': 'USER supprimé avec succès'})

if __name__ == '__main__':
    app.run()
