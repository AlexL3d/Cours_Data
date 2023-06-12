import requests
import json
import time
import random

def Actual_Time():
     #Récupération du TimeStamp actuel pour appel sur la page du site
    ActualTimeStamp = int(time.time())
    return ActualTimeStamp

def TimeDelay (): 
    #Création d'une variable de délai randommisée entre 0 et 5 secondes
    delai = time.sleep(random.random()*5)

def Random_User_Agent():
    #Liste de Users Agents :
    List_User_Agent = [
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1",
                        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                    ]

    Random_User_Agent = random.choice(List_User_Agent)

    return Random_User_Agent

def FindLineGroup():
    # Definition de l'URL pour récupérer les différents codes
    url = ("https://elines.coscoshipping.com/ebbase/public/general/findLineGroup?timestamp=" + str(Actual_Time()))

    # Récupération du Json avec les données des groupes
    response = requests.get(url,headers=Random_User_Agent())

    if response.ok:
        # Transformation des données récupérées en format Json
        List_Group = response.text
        List_Group_json = json.loads(List_Group)

        # Création de la liste des codes groupe
        List_Code_Group = [item["code"] for item in List_Group_json["data"]["content"]]

    return List_Code_Group,response

def FindLine(codes):

    List_Codes = []
    for index in codes:

        # Definition de l'URL pour récupérer les différents codes
        url = ("https://elines.coscoshipping.com/ebbase/public/general/findLines?lineCode=" + str(index) + "&timestamp=" + str(Actual_Time()))

        # Récupération du Json avec les données des groupes
        response = requests.get(url,headers=Random_User_Agent()) 


        if response.ok:
            # Transformation des données récupérées en format Json
            List_Line = response.text
            List_Line_json = json.loads(List_Line)

            # Création de la liste des codes groupe
            List_Code_Line = [item['code'] for item in List_Line_json["data"]["content"]]
            List_Codes.append(List_Code_Line)

        TimeDelay()

    return List_Codes,response

def FindBoat(codes):

    List_Boats = []
    for index in codes :

        # Definition de l'URL pour récupérer les différents codes
        url = ("https://elines.coscoshipping.com/ebbase/public/vesselParticulars/search?pageSize=9999&state=lines&code=" + str(index) + "&timestamp=" + str(Actual_Time()))

        # Récupération du Json avec les données des groupes
        response = requests.get(url,headers=Random_User_Agent())


        if response.ok:
            # Transformation des données récupérées en format Json
            List_Line = response.text
            List_Line_json = json.loads(List_Line)
            print(List_Line_json)

        # Création de la liste des infos pour chaque bateau
            List_Code_Line = [item for item in List_Line_json["data"]["content"]]
            List_Boats.append(List_Code_Line)

        TimeDelay()

    return List_Boats

# ===== Test =====
Codes,code_retour = FindLineGroup()

if code_retour.ok :
    Lines,code_retour = FindLine(Codes)

if code_retour.ok :  
    List_Boats = FindBoat(Lines)

# Création du fichier contenant toutes les infos des Bateaux et des Schedules
with open('Projet_Sinay/Shedule_Boat.txt', 'w') as file:
    file.write(f"{List_Boats}")
