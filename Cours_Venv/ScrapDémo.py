""" Programme de démo de Scraping
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


def recupData():
    """ Récupération des données d'un site démo construit exprès pour ça
    """
    bookscrap = chargementEnv("BOOKSCRAP")
    url = bookscrap + "catalogue/page-1.html"

    response = get(url)
    return response.content


def scrapBs():
    """ Scraping avec BeautifulSoup
    """

    MaPage = recupData()
    soup = Bs(MaPage, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')

    with open('save_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        headers = ["Titre", "Note", "Prix"]
        writer.writerow(headers)

        for article in articles:
            image = article.find('img')
            titre = image['alt']
            print("titre : ", titre)
            star = article.find('p')
            star = star["class"][1]
            print("Note : ", star, "sur 5")
            prix = article.find('p', class_='price_color').text
            print("Prix (en {}) du livre : {}").format(prix[:1],prix[1:])
            writer.writerow([titre, note, prix[1:]])

            with open('save_data.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([titre, note, prix[1:]])

if __name__ == "__main__":
    # recupData()
    scrapBs()
