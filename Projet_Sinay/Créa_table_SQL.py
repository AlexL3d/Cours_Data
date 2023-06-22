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

def Use_Bdd(conn: Connexion, database_name: str):
    # Création du curseur
    cursor = conn.cursor()

    # Sélection de la base de données nouvellement créée
    use_database_query = f"USE {database_name}"
    cursor.execute(use_database_query)


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


def Close_Connexion(conn: Connexion):
    # Fermeture de la connexion
    conn.close()


if __name__ == '__main__':

    # Connexion à la base SQL
    Connect = Connexion()

    # Utilisation de la BDD spécifiée
    BaseDeDonnées_Spe = Use_Bdd(Connect, database_name=databases)

    # Création de la table Test
    database = "BDD_Test"
    Crea_table_Tests = Crea_table(Connect, database_name=database)

    # Fermeture de la connexion à la base de données
    Fermeture = Close_Connexion(Connect)
