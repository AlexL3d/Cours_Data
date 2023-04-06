#FONCTIONS 

#Saisie du nombre  
def Saisie() -> int :
    entrée = int(input("Entrez un votre âge : "))

    while entrée < 1 :
        entrée = int(input("Entrez votre âge : "))
    return entrée

#Catégorie d'âge
def Catégorie () :
    age = Saisie()

    if age >= 12 :
        print ('Cadet')
    elif age >=10 :
        print ("Minime")
    elif age >= 8 : 
        print ('Pupille')
    else : 
        print ('Poussin')

#MAIN 
Catégorie()