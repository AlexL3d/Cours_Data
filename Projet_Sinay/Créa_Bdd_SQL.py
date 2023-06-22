import mysql.connector


def Connexion():
    # Établir une connexion à la base de données MySQL
    # Informations de connexion
    host = 'localhost'
    user = 'root'
    password = 'SINAY'
    port = '3308'

    # Création de la connexion
    conn = mysql.connector.connect(
        host=host,
        user=user,
        port=port,
        password=password
    )

    # Test de connexion
    if conn.is_connected():
        print('Connecté à MariaDB')
        return conn


def Crea_Bdd(conn: Connexion):
    # Création du curseur
    cursor = conn.cursor()

    # Création de la base de données
    database_name = 'BDD_Test'
    database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    cursor = conn.cursor()
    cursor.execute(database_query)
    return database_name


def Close_Connexion(conn: Connexion):
    # Fermeture de la connexion
    conn.close()

############ MAIN ##############


if __name__ == '__main__':
    # Connexion à la base SQL
    Connect = Connexion()

    # Création de la database
    Crea_BDD = Crea_Bdd(Connect)

    # Fermeture de la connexion à la base de données
    Fermeture = Close_Connexion(Connect)
