import random

def CréationTableau () :
    arr = []

    for i in range(500):
        arr.append(random.randrange(0,1000))

    return arr
    
def RechercheLinéaire () :
    arr = CréationTableau()
    booléen = False

    for index in range(len(arr)) :
        if arr[index] == 42 :
            print(f"Le chiffre 42 se trouve à l'index {index}. ")
            booléen = True
        
    if not booléen :
        print("Le chiffre 42 n'est pas dans la liste.")

RechercheLinéaire()
