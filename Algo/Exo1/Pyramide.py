#FONCTIONS ===========================

#Saisie du nombre  
def Saisie() -> int :
    entrée = int(input("Entrez un nombre entier positif non-nul : "))

    while entrée <=0 :
        entrée = int(input("Entrez un nombre entier positif non-nul : "))
    return entrée

def Pyramide () :

    nombre = Saisie()
    affichage = ""
    space = ' '
    étoiles = '* '

    for index0 in range (nombre+1) :
        for index1 in range (nombre+1-index0) :
            affichage += space
        for index2 in range (index0) :
            affichage += étoiles
        affichage += "\n"
    print (affichage)
    
#MAIN

Pyramide ()