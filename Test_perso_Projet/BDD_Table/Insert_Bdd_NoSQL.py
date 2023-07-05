
from pymongo import MongoClient
import ConnectionDatabaseNoSQL as CDB


def Crea_collection(Bdd):
    # Créer une collection
    collection = Bdd['collection']
    return collection


def Insertion_collection(collection):
    # Insérer des données
    data = {
        'content':
            {
                'nom': 'John Doe',
                'age': 30,
                'ville': 'Paris'
            },
            'villes':
            {
                'nom': 'Lille',
                'Latitude': 12,
                'longitude': 3
            }
    }
    collection.insert_one(data)


if __name__ == '__main__':

    # Connexion à la base MongoDB
    conn = CDB.Connexion()

    print("Connexion à la base MongoDB réussie")

    # Création de la collection
    collection = Crea_collection(Bdd)

    # Création d'un data et insertion dans la collection
    Insert = Insertion_collection(collection)

    # Fermeture de la connexion
    conn.close()
