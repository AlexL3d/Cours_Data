from ExportData.CsvUse import HeadersCSV, EcritureData
import requests
import time
import json
from HTTP.RandomAgent import RandomAgent
from HTTP.CheckerHTTP import RequestChecker

TimeStampATM = int(time.time())

def GetNumberTrade()->list:
    """
    Le but ici est d'avoir la liste des codes des trades. Si le site rajoute un code il sera detecte
    ex: America Service = code=1

    Returns:
        list: Retourne une liste de code de trade
    """
    
    url = 'https://elines.coscoshipping.com/ebbase/public/general/findLines?lineCode=0&timestamp='
    CptIterate = 0
    NomCSV = "NumberTrade.csv"
    ListeElementHeaders = ["ID_TRADE", "NAME_TRADE"]
    code_values = []
    
    HeadersCSV(NomCSV, ListeElementHeaders)
    
    print("GetNumberTrade() is running =>")
    
    # URL du site en code 0 pour avoir tous les codes disponible
    ParseNumberLine = requests.get(url+str(TimeStampATM), headers=RandomAgent())
    
    if RequestChecker(ParseNumberLine) == 1:
        # Transformation de la requête en JSON 
        data = json.loads(ParseNumberLine.text)
        
        # Récupération du contenu des items 'code' dans le JSON 
        code_values = [item['code'] for item in data['data']['content']]

        for element in code_values:
            EcritureData(NomCSV, element)
            CptIterate += 1
        
        print(f"    Done with {CptIterate} codes !")
        
    else:
        code_values = ["Response failed"]
        EcritureData(NomCSV, code_values)

    return code_values