#FONCTIONS 

#Saisie du nombre  
def Saisie() -> int :
    entrée = int(input("Entrez un nombre entier positif non-nul : "))

    while entrée <=0 :
        entrée = int(input("Entrez un nombre entier positif non-nul : "))
    return entrée

#Détermination si puissance de 2 il y a 
def Puissance() :
    nombre = Saisie()
    nbrtmp = nombre
    cpt = 0

    while nbrtmp % 2 == 0:
        nbrtmp //= 2 
        cpt += 1
    
    if nbrtmp == 1:
        print (f"Le nombre {nombre} est une puissance de 2 : 2^{cpt}")
    else :
        print (f"Le nombre {nombre} n'est pas une puissance de 2")

#MAIN
Puissance()
