""" Programme de scraping d'avocats
"""

# Importation des librairies
from dotenv import load_dotenv
import os
from requests import get
from bs4 import BeautifulSoup as Bs
import csv


def chargementEnv(varEnv: str):
    """ Charge les variables d'environnement
    """
    load_dotenv()
    return os.getenv(varEnv)


def recupData(index):
    """ Récupération des données d'un site démo construit exprès pour ça
    """
    avocats = chargementEnv("AVOCATS")
    url = avocats + f"?fwp_paged={index}"

    response = get(url)
    return response.content


def ListeAvocats():
    """ Récupération des données d'un site d'avocats
    """

    with open('./Cours_Venv/Exo_Avocats/Liste_Avocats.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        headers = ["Nom et Prenom", "Adresse", "Email", "Telephone"]
        writer.writerow(headers)

    for index in range(1, 51):
        MaPage = recupData(index)
        soup = Bs(MaPage, 'html.parser')
        Datas = soup.find_all(
            'div', class_="callout secondary annuaire-single")

        for Data in Datas:

            # Nom et Prénom
            Nom_Prenom = Data.find('h3', class_="nom-prenom").text.strip()
            Nom_Prenom = Nom_Prenom.replace('"', '')

            # Adresse
            Adresse = Data.find(
                'span', class_="adresse").text.strip()
            Adresse = Adresse.replace('"', '')
            Adresse = Adresse.replace(',', '')
            Adresse = " ".join(Adresse.split())

            # Téléphone
            Téléphone = Data.find('span', class_="telephone").text.strip()
            Téléphone = Téléphone[4:]

            # Email
            Infos = Data.find('span', class_="email")
            try:
                Email = Infos.find('a').text.strip()
            except AttributeError:
                Email = "Introuvable"

            # Ecriture dans le fichier CSV
            with open('./Cours_Venv/Exo_Avocats/Liste_Avocats.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow([Nom_Prenom, Adresse, Email, Téléphone])


if __name__ == "__main__":
    ListeAvocats()
