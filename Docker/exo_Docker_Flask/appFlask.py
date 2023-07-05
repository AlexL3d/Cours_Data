from flask import Flask, request, jsonify
from pymongo import MongoClient

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client[Bdd_user]  
collection = db[users] 

app = Flask(__name__)

# Route pour créer un nouvel élément
@app.route('/item', methods=['POST'])
def create_item():
    item = request.get_json()
    collection.insert_one(item)
    return jsonify({'message': 'Nouveau USER créé avec succès'})

# Route pour récupérer tous les éléments
@app.route('/items', methods=['GET'])
def get_all_items():
    items = list(collection.find())
    return jsonify(items)

# Route pour récupérer un élément par son ID
@app.route('/item/<item_id>', methods=['GET'])
def get_item(item_id):
    item = collection.find_one({'_id': ObjectId(item_id)})
    return jsonify(item)

# Route pour mettre à jour un élément
@app.route('/item/<item_id>', methods=['PUT'])
def update_item(item_id):
    new_item = request.get_json()
    collection.update_one({'_id': ObjectId(item_id)}, {'$set': new_item})
    return jsonify({'message': 'USER mis à jour avec succès'})

# Route pour supprimer un élément
@app.route('/item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    collection.delete_one({'_id': ObjectId(item_id)})
    return jsonify({'message': 'USER supprimé avec succès'})

if __name__ == '__main__':
    app.run()
