import time
import random
import requests
import json
from ExportData.CsvUse import HeadersCSV, EcritureData
from HTTP.RandomAgent import RandomAgent
from HTTP.CheckerHTTP import RequestChecker

TimeStampATM = int(time.time())

def GetSchedules(CodeVessels: dict) -> dict:
    """
    Récupération des schedules de tous les bateaux si il n'y en a pas, retourne "Null" sinon chaque Schedules sont retournés

    Returns:
        dict: _description_
    """
    cptIterateSchedules = 0
    cptIterateVessel = 0
    DictionnaireVessel = {}
    out_file = open("./Data/json/Schedules.json", "w")
    cpt = 0
    NomCSV = "Schedules.csv"
    Headers = ["id", "loopAbbrv", "vesselCode", "vesselName", "voy", "protName",
               "uvrn", "arrDtlocAct", "depDtlocAct", "arrDtlocCos", "depDtlocCos"]

    HeadersCSV(NomCSV, Headers)

    print("GetSchedules() is running =>")

    for valeur in CodeVessels.values():
        ListeVal = []
        # Attente pour ne pas se faire repérer
        TempsEnvoi = int(random.randint(1, 3))
        time.sleep(TempsEnvoi)

        # Parse de tous les navires avec leurs infos
        ParseVesselAll = requests.get('https://elines.coscoshipping.com/ebschedule/public/purpoShipment/vesselCode?vesselCode='+str(
            valeur)+'&period=28&timestamp='+str(TimeStampATM), headers=RandomAgent())

        if RequestChecker(ParseVesselAll) == 1:
            # Transformation de la requête en JSON
            data = json.loads(ParseVesselAll.text)

            # Vérification du contenu de la page afin de ne pas récupérer une page vide
            if data['data']['content'] is None:
                DictionnaireVessel[valeur] = ["Null"]
                EcritureData(NomCSV, [valeur, "Null"])
            else:
                for item in data['data']['content']['data']:
                    ListeVal.append(item)
                    cpt += 1  # A supprimer en prod
                    ListeElements = [item["id"], item["loopAbbrv"], item["vesselCode"], item["vesselName"], item["voy"],
                                     item["protName"], item["uvrn"], item["arrDtlocAct"], item["depDtlocAct"], item["arrDtlocCos"], item["depDtlocCos"]]

                    EcritureData(NomCSV, ListeElements)
                    cptIterateSchedules += 1

                DictionnaireVessel[str(item['vesselCode'])] = ListeVal

            cptIterateVessel += 1

        cpt += 1  # A supprimer en prod
        if cpt >= 3:
            break

    json.dump(DictionnaireVessel, out_file)

    print(
        f"    Done with {cptIterateSchedules} Schedules for {cptIterateVessel} vessels !")

    return (DictionnaireVessel)
