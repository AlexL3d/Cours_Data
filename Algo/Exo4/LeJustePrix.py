#Importation de la fonction random
import random

#Saisie du nombre
def Saisie() -> int :
    entrée = int(input("Entrez un nombre positif non-nul : "))

    while entrée <= 0 :
        entrée = int(input("Entrez un nombre positif non-nul : "))
    return entrée

# Test de la valeur de l'utilisateur
def Test(nbrrand:int) :
    cpt = 10

    while cpt > 0 :
        nombre=Saisie()
        
        if nombre < nbrrand :
            print ("C'est PLUS !")
          
        elif nombre > nbrrand :
            print("C'est MOINS !")
            
        else :
            print("C'est GAGNÉ !")
            break
            
        cpt -= 1    
        print(f"Il reste {cpt} tentatives.")
    
    if cpt == 0 :
        print(f"C'est PERDU ! Le nombre était : {nbrrand}.")

# MAIN ============================

#Calcul du nombre aléatoire
nbrrandom = random.randint(1,1000)

#Test de recherche du nombre exact
Test(nbrrandom)