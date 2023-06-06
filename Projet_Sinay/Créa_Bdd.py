import mysql.connector


def Connexion():
    # Établir une connexion à la base de données MySQL
    # Informations de connexion
    host = 'localhost'
    user = 'Alex'
    password = 'SINAY'
    database = 'TestDB'

    # Création de la connexion
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )


def Créa_Bdd():
    # Création de la base de données
    database_name = 'BDD_Test'
    create_database_query = f"CREATE DATABASE {database_name}"
    cursor = conn.cursor()
    cursor.execute(create_database_query)


def Créa_table():
    # Création d'une table
    create_table_query = """
    CREATE TABLE Tests (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nom VARCHAR(100),
        email VARCHAR(100)
    )
    """
    cursor.execute(create_table_query)


def Use_Bdd():
    # Sélection de la base de données nouvellement créée
    use_database_query = f"USE {database_name}"
    cursor.execute(use_database_query)


def Close_Connexion():
    # Fermeture de la connexion
    conn.close()

############ MAIN ##############

    # Connexion à la base SQL
    Connect = Connexion()

    # Création de la database
    Créa_BDD = Créa_Bdd()

    # Création de la base de données Test
    # Créa_table_Tests = Créa_table()

    # Fermeture de la connexion à la base de données
    # Fermeture = Close_Connexion()
