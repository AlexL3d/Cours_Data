import mysql.connector
import ConnectionDatabaseSQL as CD


    # host = 'localhost'
    # user = 'root'
    # password = 'SINAY'
    # port = '3308'

def Crea_Bdd(conn: Connexion, name: str):
    # Création du curseur
    cursor = conn.cursor()

    # Création de la base de données
    try :
        database_name = "name"
        database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
        cursor = conn.cursor()
        cursor.execute(database_query)

    except mysql.connector.Error as err:
        print("Erreur lors de la création de la base de données : {}".format(err))


############ MAIN ##############


if __name__ == '__main__':
    # Connexion à la base SQL
    Connect = CD.ConnectDB()

    # Création de la database
    Crea_BDD = Crea_Bdd(Connect, "BDD_test")

    # Fermeture de la connexion à la base de données
    conn.close()
