import mysql.connector
import json


def Connexion():
    # Établir une connexion à la base de données MySQL
    # Informations de connexion
    host = 'localhost'
    user = 'Alex'
    password = 'SINAY'
    port = '3308'

    # Création de la connexion
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cursor = conn.cursor()
    
    # Test de connexion
    if conn.is_connected():
        print('Connecté à MariaDB')
        return conn


def Validation_Changement(conn: Connexion):
    # Valider les changements
    conn.commit()


def Close_Connexion(conn: Connexion):
    # Fermer la connexion à la base de données
    conn.close()


def Insertion(data: json):
    ############ EXAMPLE ############
    # Parcourir les données JSON et les insérer dans la base de données
    for item in data:
        # Extraire les valeurs des champs du JSON
        field1 = item['field1']
        field2 = item['field2']
        # ... ajoutez plus de champs selon votre structure JSON et votre base de données

        # Exécuter la requête d'insertion
        query = "INSERT INTO your_table (field1, field2) VALUES (%s, %s)"
        values = (field1, field2)
        cursor.execute(query, values)


def Lect_Json() -> json:
    # Lire le fichier JSON
    with open('data.json', 'r') as file:
        json_data = file.read()

    # Charger les données JSON
    data = json.loads(json_data)
    return data

############ MAIN ##############

#meture = Close_Connexion()
