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


def Crea_table(conn: Connexion, database_name: str):
    # Création du curseur
    cursor = conn.cursor()

    # Création d'une table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Tests (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nom VARCHAR(100),
        email VARCHAR(100)
    )
    """

    cursor.execute(create_table_query)


def Use_Bdd(conn: Connexion, database_name: str):
    # Création du curseur
    cursor = conn.cursor()

    # Sélection de la base de données nouvellement créée
    use_database_query = f"USE {database_name}"
    cursor.execute(use_database_query)


def Close_Connexion(conn: Connexion):
    # Fermeture de la connexion
    conn.close()

############ MAIN ##############


# Connexion à la base SQL
Connect = Connexion()

# Création de la database
Crea_BDD = Crea_Bdd(Connect)

# Utilisation de la BDD spécifiée
BaseDeDonnées_Spe = Use_Bdd(Connect,Crea_BDD)

# Création de la base de données Test
Crea_table_Tests = Crea_table(Connect, Crea_BDD)

# Fermeture de la connexion à la base de données
Fermeture = Close_Connexion(Connect)
