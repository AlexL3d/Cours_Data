import requests
import json
import time
import random

ActualTimeStamp = int(time.time())

def FindLineGroup() : 
    # Definition de l'URL pour récupérer les différents codes
    url = ("https://elines.coscoshipping.com/ebbase/public/general/findLineGroup?timestamp=" + str(ActualTimeStamp))
    
    # Récupération du Json avec les données des groupes
    response = requests.get(url)
    
    if response.ok : 
        # Transformation des données récupérées en format Json
        List_Group = response.text
        List_Group_json = json.loads(List_Group)
        
        # Création de la liste des codes groupe
        List_Code_Group = [item["code"] for item in List_Group_json["data"]["content"]]
        
        return List_Code_Group
    
def FindLine(codes) :
    
    List_Boats = []
    for index in codes :
    
        # Definition de l'URL pour récupérer les différents codes
        url = ("https://elines.coscoshipping.com/ebbase/public/general/findLines?lineCode=" + str(index) + "&timestamp=" + str(ActualTimeStamp)).time()
        
        # Récupération du Json avec les données des groupes
        response = requests.get(url)
        
        if response.ok : 
            # Transformation des données récupérées en format Json
            List_Line = response.text
            List_Line_json = json.loads(List_Line)
            # Création de la liste des codes groupe
            List_Code_Line = [item for item in List_Line_json["data"]["content"]]
            
            List_Boats.append(List_Code_Line)
            return List_Boats
        
        
# ===== Test =====
# Codes = FindLineGroup()
# Lines = FindLine(Codes)

delay = random.random() * 3
print(delay)