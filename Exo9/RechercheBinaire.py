#IMPORT
import random

#FONCTIONS
def CréationTableau () :
    arr = []

    for i in range(500):
        arr.append(random.randrange(0,1000))

    arr.sort()

    print (arr)
    
    return arr
    
def RechercheBinaire (arr:list) :
    tab = []
    elem = 42
    booleen = False 
    moitié = len(arr)//2
      
    while not booleen :

        if len(arr) != 0 : 
            if arr[moitié] > elem : 
                for index in range (moitié) :
                    tab.append(arr[index])
                booleen=RechercheBinaire(tab)
            
            elif arr[moitié] < elem :
                for index in range (moitié+1,len(arr)) :
                    tab.append(arr[index])
                booleen=RechercheBinaire(tab)

            else :
                print(f"Le chiffre 42 est présent dans la liste.")
                booleen = True

        else :
            print(f"Le chiffre 42 n'est pas présent dans la liste.")
            booleen = True 

        return booleen    

#MAIN
arr = CréationTableau()
RechercheBinaire(arr)