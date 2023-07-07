# Exemple de communication à MongoDB
# Base de données = Database 
# table = Collection
# row = Document


# Importation des librairies
from pymongo import MongoClient

# Informations de ma base de données
host = "localhost"
port = 27017

# Création de la connexion
connexion = MongoClient(host=host, port=port)

#Récupération de la base de données
bdd = connexion.Bdd_user
print("Bdd_user: \n", bdd)

#Récupération de la collection
collection = bdd.User
print("Collection: \n", collection)

#Ajout d'un document => format JSON
data_user = {
    "name": "Jean",
    "firstname": "Jean-Luc",
    "age": "25"
}
response = collection.insert_one(data_user)

# Récupération de l'ID à partir de l'objectID
new_id = str(response.inserted_id)

# Attribution de son ID à mon document
data_user["id"] = new_id
print("user: \n", data_user)

# Récupération de tous les documents
users = collection.find()
print("users: \n", list(users))

# Récupération d'un document
user = collection.find_one({'name' : 'Jean'})
print("user \n", str(user))

