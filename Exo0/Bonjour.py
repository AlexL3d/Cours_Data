#FONCTIONS 

#Saisie du nom
def Saisie() -> int :
    entrée = input("Entrez un votre âge : ")

    while entrée < 1 :
        entrée = input("Entrez votre âge : ")
    return entrée

#HELLO WORLD
def Bonjour () :

    nom = Saisie ()

    print(f"Bonjour {nom} ! ")

#MAIN 
Bonjour ()