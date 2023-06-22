from pymongo import MongoClient
import ConnectionDatabaseNoSQL as CDB


def Lecture_Collection(collection):
    # Lire tous les documents dans la collection
    documents = collection.find()
    for doc in documents:
        print(doc)


if __name__ == "__main__":

    # Connexion à la base MongoDB
    conn = CDB.Connexion()

    print("Connexion à la base MongoDB réussie")

    # Lecture des données en BDD
    Lect = Lecture_Collection(collection)

    # Fermeture de la connexion à la base MongoDB
