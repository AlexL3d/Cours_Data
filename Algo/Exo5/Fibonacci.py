#FONCTIONS ===========================
#Saisie du nombre d'itérations
def Saisie() -> int :
    entrée = int(input("Entrez un nombre entier positif non-nul : "))

    while entrée <=0 :
        entrée = int(input("Entrez un nombre entier positif non-nul : "))
    return entrée

def Fibonacci () :
    listeFibonacci=[0,1]
    nombreitération = Saisie()

    for index in range (2,nombreitération):
        listeFibonacci.append(listeFibonacci[index-1]+listeFibonacci[index-2])
    
    print(listeFibonacci)

#MAIN =================================
Fibonacci()
