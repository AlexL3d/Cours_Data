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
                        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                        "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)",
                        "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
                        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
                        "Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
                        "Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
                        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
                        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]",
                        "Mozilla/5.0 (Windows NT 6.1; rv:2.0b7pre) Gecko/20100921 Firefox/4.0b7pre",
                        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322)",
                        "Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                        "Mediapartners-Google",
                        "magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
                        "Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://ahrefs.com/robot/)",
                        "Mozilla/5.0 (compatible; Ezooms/1.0; ezooms.bot@gmail.com)",
                        "Mozilla/5.0 (compatible; proximic; +http://www.proximic.com/info/spider.php)",
                        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
                        "Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)",
                        "Sosospider+(+http://help.soso.com/webspider.htm)",
                        "msnbot/2.0b (+http://search.msn.com/msnbot.htm)",
                        "Wotbox/2.01 (+http://www.wotbox.com/bot/)",
                        "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
                    ]

    Random_User_Agent = {"User-Agent" : random.choice(List_User_Agent)}

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

    #Transformation de la liste des listes de codes en liste
    List_codes = [code for List in codes for code in List]

    # Boucle d'appels sur la liste des codes
    for index in List_codes :

        # Definition de l'URL pour récupérer les différents codes
        url = ("https://elines.coscoshipping.com/ebbase/public/vesselParticulars/search?pageSize=9999&state=lines&code=" + str(index) + "&timestamp=" + str(Actual_Time()))

        # Récupération du Json avec les données des groupes
        response = requests.get(url,headers=Random_User_Agent())

        if response.ok:
            # Transformation des données récupérées en format Json
            List_Line = response.json()

            # Création de la liste des infos pour chaque bateau
            List_Boats.append(List_Line["data"]["content"])


        TimeDelay()

    # Création du fichier contenant toutes les infos des Bateaux et des Schedules
    with open('Projet_Sinay/List_Boat.json', 'w') as file:
        file.write(f"{List_Boats}")


    return List_Boats,response

def ScheduleBoat(List_Boat):
    
    List_Schedule_Boats = []
    Test = List_Boat[0][0]

    for liste in List_Boat:
        for dictionnaire in liste:
                        
            # Definition de l'URL pour récupérer les différents codes
            url = ("https://elines.coscoshipping.com/ebschedule/public/purpoShipment/vesselCode?vesselCode=" + str(dictionnaire["VesselCode"]) + "&period=28&timestamp= " + str(Actual_Time()))
            
            # Récupération du Json avec les données des groupes
            response = requests.get(url,headers=Random_User_Agent())

            if response.ok:
                # Transformation des données récupérées en format Json
                List_Line = response.json()

                # Création de la liste des infos pour chaque bateau
                List_Schedule_Boats.append(List_Line["data"]["content"])


            TimeDelay()

    return List_Boats

def main(): 
    """Méthode de déclenchement de mes fonctions d'appel au site
    """
    Codes,code_retour = FindLineGroup()

    if code_retour.ok :
        Lines,code_retour = FindLine(Codes)

    if code_retour.ok :  
        List_Boats,code_retour = FindBoat(Lines)

    if code_retour.ok :
        List_Schedule = ScheduleBoat(List_Boats)

    # Création du fichier contenant toutes les infos des Bateaux et des Schedules
    with open('Projet_Sinay/Shedule_Boat.json', 'w') as file:
        file.write(f"{List_Schedule}")


# ===== Test =====
main()