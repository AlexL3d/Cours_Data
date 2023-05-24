import requests
from bs4 import BeautifulSoup

links=[]
url = "https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde"

response = requests.get(url)

if response.ok :
    soup = BeautifulSoup(response.text, features='html.parser')
    tds = soup.find_all('td')
    for td in tds :
        a = td.find("a")
        link = a["href"]
        links.append('https://fr.wikipedia.org' + link)

with open('TestScraping/url.txt','w') as file :
    for link in links :
        file.write(f"{link} \n")
        
# with open('url.txt','r') as file :
#     for row in file :
#         print(row)