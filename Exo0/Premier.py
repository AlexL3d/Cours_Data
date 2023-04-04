#FONCTIONS 

#Saisie du nombre  
def Saisie() -> int :
    
    entrée = int(input("Entrez un nombre entier positif non-nul : "))

    while entrée < 1 :
        entrée = int(input("Entrez un nombre entier positif non-nul : "))
    return entrée

def Premier() :
    
    nombre = Saisie ()
    cpt = 0 
    moitié = nombre // 2

    for diviseur in range (2,moitié) :
        if nombre%diviseur == 0 :
            cpt += 1

    if cpt != 0 :
        print(f"Le nombre {nombre} n'est pas premier.")
    else :
        print(f"Le nombre {nombre} est premier ! ")

#MAIN
Premier()