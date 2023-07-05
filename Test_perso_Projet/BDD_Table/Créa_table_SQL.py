import mysql.connector
import ConnectionDatabaseSQL as CD


    # host = 'localhost'
    # user = 'root'
    # password = 'SINAY'
    # port = '3308'


def Use_Bdd(conn: Connexion, database_name: str):
    # Création du curseur
    cursor = conn.cursor()

    # Sélection de la base de données nouvellement créée
    use_database_query = f"USE {database_name}"
    cursor.execute(use_database_query)


def Crea_table_Schedule(conn: Connexion, database_name: str):

    Bdd = Use_Bdd(conn, database_name)

    # Création du curseur
    cursor = conn.cursor()

    try :
        # Création d'une table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS SCHEDULE (
            id INT PRIMARY KEY AUTO_INCREMENT,
            arrDtlocAct DATETIME,
            DepDtlocAct DATETIME,
            arrDtlocCos DATETIME,
            DepDtlocCos DATETIME,
            idVessel INT,
            idPort INT;
        )
        """

        cursor.execute(create_table_query)

    except mysql.connector.Error as err:
        print("Erreur lors de la création de la table SCHEDULE: {}".format(err)) 

def Crea_table_Vessel(conn: Connexion, database_name: str):

    Bdd = Use_Bdd(conn, database_name)

    # Création du curseur
    cursor = conn.cursor()

    try :
        # Création d'une table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS VESSEL (
            idVessel INT PRIMARY KEY AUTO_INCREMENT,
            nameVessel VARCHAR(45),
            Lloyds INT,
            flagCountry VARCHAR(45),
            yearBuilt YEAR,
            callSign VARCHAR(20),
            idService INT,
            idTrade INT;
        )
        """

        cursor.execute(create_table_query)

    except mysql.connector.Error as err:
        print("Erreur lors de la création de la table VESSEL: {}".format(err)) 

def Crea_table_Trade(conn: Connexion, database_name: str):

    Bdd = Use_Bdd(conn, database_name)

    # Création du curseur
    cursor = conn.cursor()

    try :
        # Création d'une table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS TRADE (
            idTrade INT PRIMARY KEY AUTO_INCREMENT,
            nameTrade VARCHAR(45);
        )
        """

        cursor.execute(create_table_query)

    except mysql.connector.Error as err:
        print("Erreur lors de la création de la table TRADE: {}".format(err)) 

def Crea_table_Service(conn: Connexion, database_name: str):

    Bdd = Use_Bdd(conn, database_name)

    # Création du curseur
    cursor = conn.cursor()

    try :
        # Création d'une table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS SERVICE (
            idService INT PRIMARY KEY AUTO_INCREMENT,
            nameService VARCHAR(45),
            codeService VARCHAR(45);
        
        """

        cursor.execute(create_table_query)

    except mysql.connector.Error as err:
        print("Erreur lors de la création de la table SERVICE: {}".format(err)) 

def Crea_table_Port(conn: Connexion, database_name: str):

    Bdd = Use_Bdd(conn, database_name)

    # Création du curseur
    cursor = conn.cursor()

    try :
        # Création d'une table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS PORT (
            idPort INT PRIMARY KEY AUTO_INCREMENT,
            namePort VARCHAR(45),
            long VARCHAR(45),
            lat VARCHAR(45);
        
        """

        cursor.execute(create_table_query)

    except mysql.connector.Error as err:
        print("Erreur lors de la création de la table PORT: {}".format(err)) 


if __name__ == '__main__':

    # Connexion à la base SQL
    Connect = Connexion()

    # Création de la table Test
    database = "BDD_SINAY"
    Crea_table_ = Crea_table(Connect, database_name=database)

    # Fermeture de la connexion à la base de données
    conn.close()
