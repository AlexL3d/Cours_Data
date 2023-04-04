#IMPORT
import random

#FONCTIONS
def CréationTableau () :
    arr = []

    for i in range(500):
        arr.append(random.randrange(0,1000))

    return arr.sort()
    
def RechercheBinaire (arr:list) :
    tab = []
    elem = 42
    booleen = False 
    moitié = len(arr)//2

    while not booleen :

        if arr[moitié] < elem : 
            if len(arr) == 1 :
                print(f"Le chiffre 42 est absent de la liste.")
                booleen = True
            else : 
                for index in range (moitié) :
                    tab.append(arr[index])
                RechercheBinaire(tab,moitié)
            
        elif arr[moitié] > elem :
            if len(arr) == 1 :
                print(f"Le chiffre 42 est absent de la liste.")
                booleen = True
            else :    
                for index in range (moitié,len(arr),1) :
                    tab.append(arr[index])
                RechercheBinaire(tab,moitié)    

        else :
            print(f"Le chiffre 42 est présent dans la liste.")
            booleen = True

#MAIN
arr = CréationTableau()
RechercheBinaire(arr)