#FONCTIONS

def Saisie():

    tab=[]

    while len(tab) != 3 :
        numbers = input ("Entrez la longueur des 3 côtés du triangle : ")
        tab = numbers.split()
    
    return tab

def Pythagore () :

    tab = Saisie()

    if (int(tab[0])**2 + int(tab[1])**2 == int(tab[2])**2) or (int(tab[1])**2 + int(tab[2])**2 == int(tab[0])**2) or (int(tab[0])**2 + int(tab[2])**2 == int(tab[1])**2) :
        print("Le triangle est rectangle.")
    else :
        print("Le triangle n'est pas rectangle.")

#MAIN
Pythagore()

