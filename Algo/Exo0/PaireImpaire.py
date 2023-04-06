#FONCTIONS 

#Saisie du nombre  
def Saisie() -> int :
    entrée = int(input("Entrez un nombre entier positif non-nul : "))

    while entrée <=0 :
        entrée = int(input("Entrez un nombre entier positif non-nul : "))
    return entrée

def PaireImpaire () :

    nombre = Saisie()

    if nombre % 2 :
        print (f"le nombre {nombre} est impaire.")
    else :
        print (f"le nombre {nombre} est pair.")

#MAIN 
PaireImpaire()