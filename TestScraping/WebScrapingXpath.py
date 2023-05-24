import requests
from lxml import etree
from bs4 import BeautifulSoup

links=[]
url = "https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde"

response = requests.get(url)

if response.ok :
    soup = BeautifulSoup(response.content, features='html.parser')
    dom = etree.HTML(str(soup))
    print(dom.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[3]/td[2]/a')[0].text)
