from pymongo import MongoClient
from pymongo.errors import OperationFailure
import Créa_Bdd_NoSQL as Créa_Bd

def Connexion():
    try:
        # Se connecter à MongoDB
        conn = MongoClient('mongodb://localhost:27017/')
        return conn
    except pymongo.errors.ConnectionError as e:
        print("Errreur de la connexion à MongoDB : ", e)

if __name__ == '__main__':
    conn = Connexion()