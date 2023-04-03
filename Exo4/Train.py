#FONCTIONS =====================
def Tchoutchou (vitesse : int) -> str: 
    minute = (60*170//vitesse) % 60
    heure = 9 + (170//vitesse)
    time = str(heure) + "H" + str(minute)
    
    return time

def ListeVitesse () : 
    listeV = []
    for index in range(100,301,10) :
        listeV.append(index)
    
    return listeV

def CalculHeurePassage () :
    listeV = ListeVitesse()
    listeH =[]

    for index in range (len(listeV)) :
        HeureP = Tchoutchou(listeV[index])
        listeH.append(HeureP)

    for index in range (len(listeV)) :
        print (f"A {listeV[index]} km/h,le train arrivera à {listeH[index]}.")

#MAIN ========================
CalculHeurePassage()