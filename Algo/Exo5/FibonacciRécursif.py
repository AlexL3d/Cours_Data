#FONCTIONS ===========================
#Saisie du nombre d'itérations
def Saisie() -> int :
    entrée = int(input("Entrez un nombre entier positif non-nul : "))

    while entrée <=0 :
        entrée = int(input("Entrez un nombre entier positif non-nul : "))
    return entrée

def Fibonacci (itération) :
    
    if itération == 0 or itération == 1 :
        return 1
    else :
        return (Fibonacci(itération-1)+Fibonacci(itération-2))
  
#MAIN ================================
listeFibonacci=[0,1]
nombreIteration = Saisie()

for index in range (2,nombreIteration) :
    listeFibonacci.append(Fibonacci(index))

print (listeFibonacci)