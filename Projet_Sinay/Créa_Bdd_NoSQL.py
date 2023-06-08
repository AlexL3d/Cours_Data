from pymongo import MongoClient

def Connexion(): 
    # Se connecter à MongoDB
    conn = MongoClient('mongodb://localhost:27017/')
    return conn

def Crea_Bdd(conn: Connexion) :
    # Créer une base de données
    BaseDeDonnées = conn['BDD_Json']
    return BaseDeDonnées

def Crea_collection(Bdd) :
    # Créer une collection
    collection = Bdd['collection']
    return collection

def Insertion_collection(collection):
    # Insérer des données
    data = { 
        'content' : 
            {
            'nom': 'John Doe',
            'age': 30,
            'ville': 'Paris'
            },
            'villes' :
            {
            'nom' : 'Lille',
            'Latitude' : 12,
            'longitude' : 3
            }
    }
    collection.insert_one(data)

def Lecture_Collection(collection) :
    # Lire tous les documents dans la collection
    documents = collection.find()
    for doc in documents :
        print(doc)

#################### MAIN ########################

#Connexion à la base MongoDB 
conn = Connexion()

if 'BDD_Json' not in conn.list_database_names() :
    #Création de la base de données
    Bdd = Crea_Bdd(conn)
else :
    Bdd = conn['BDD_Json']
    
#Création de la collection
collection = Crea_collection(Bdd)

#Création d'un data et insertion dans la collection
Insert = Insertion_collection(collection)

#Lecture des données en BDD
Lect = Lecture_Collection(collection)
