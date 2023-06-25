import mysql.connector
from dotenv import load_dotenv
from mysql.connector import errorcode
import os

def LoadEnv(VARENV:str):
    """Méthode qui permet de charger une variable d'environnement à partir d'un fichier .env

    Args:
        VARENV (str): Le nom de la variable à changer

    Returns:
        _type_: Valeur de la variable
    """
    load_dotenv()
    return os.getenv(VARENV)

def ConnectDB()->mysql.connector:
    """Connction to the database and test this one
    Returns:
        mysql.connector: Retourne la database
    """
    try:
        Connection = mysql.connector.connect(user=LoadEnv("USER"), password=LoadEnv("PW"),host=LoadEnv("HOST"),database=LoadEnv("DB"), port=LoadEnv("PORT"))
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return Connection