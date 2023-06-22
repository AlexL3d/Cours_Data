import ConnectionDatabaseNoSQL as CDB
from pymongo import MongoClient

#################### METHODES ########################


def Créa_Bdd_NoSQL(conn):

    try:

        # Création de la base de données
        database_name = 'nom_de_la_base_de_donnees'
        Bdd = conn[database_name]
        return Bdd

    except PyMongoError as e:
        print("Erreur lors de la création de la base de données:", e)


#################### MAIN ########################
if __name__ == "__main__":

    # Connexion à la base MongoDB
    conn = CDB.Connexion()

    print("Connexion à la base MongoDB réussie")

    # Connexion/Création d'une base de données
    CréaBdd = Créa_Bdd_NoSQL(conn)

    # Fermeture de la connexion à la base MongoDB
    conn.close()
