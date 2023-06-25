import csv
import os

def HeadersCSV(NomDocument:str, Headers:list)->None:
    """Ecriture de l'entete CSV
    """
    try:
        os.mkdir("./Data/csv/")
    except OSError as e:
        with open("./Data/csv/"+ NomDocument, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(Headers)

def EcritureData(NomDocument, ListeHeaders:list):
    """Fonction d'ecrire de données dans le fichier CSV afin de sauvegarder les données scrapé
    Args:

    """
    try:
        os.mkdir("./Data/csv/")
    except OSError as e:
        with open("./Data/csv/"+NomDocument, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(ListeHeaders)
            file.close()