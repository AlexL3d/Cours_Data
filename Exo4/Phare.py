#FONCTIONS =============================

#Saisie du nombre
def SaisieMarches() -> int :
    entrée = int(input("Entrez un nombre de marches : "))

    while entrée <= 0 :
        entrée = int(input("Entrez un nombre positif non-nul de marches : "))
    return entrée

#Saisie de la taille des marches
def SaisieTailles() -> int :
    entrée = int(input("Entrez une taille de marches : "))

    while entrée <= 0 :
        entrée = int(input("Entrez un nombre positif non-nul pour la taille : "))
    return entrée

#Calcul de la distance par pause pipi
def CalculDistance (marches : int , taille : int) -> int :
    distance = marches * taille * 2
    return distance

#Calcul de la distance par semaine
def DistanceSemaine (distance) :
    DistanceSemaine = distance * 2 * 5 * 7
    return DistanceSemaine

#MAIN ===================================

def main () :
    marches = SaisieMarches()
    taille = SaisieTailles()
    distance = CalculDistance(marches,taille)
    distanceSemaine = DistanceSemaine(distance)

    print(f"Par semaine, il va parcourir {distance}cm.")

#AFFICHAGE DE LA TOUR
    space = '  '
    etoile = '*'
    nbétages = 0
    
    for index1 in range (0,marches,taille) :
        for index2 in range(taille,0,-1) :
            print( (index2*space) + etoile)

#Lancement du programme
main()


