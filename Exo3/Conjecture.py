def Saisie() :
    nombre = int(input("Entrez un nombre positif : "))

    while nombre <=0 :
        nombre = int(input("Entrez un nombre positif non-nul : "))  

    return nombre

def Conjecture(nombre) :
    nbétapes = 0
    while nombre != 1 :
        nbétapes +=1
        if nombre % 2 == 0 :
            nombre //= 2 
        else :
            nombre *= 3
            nombre += 1
        print (nombre)
    print (f"Il a fallu {nbétapes} étapes.")

def main() :
    Conjecture(Saisie())
    
main ()