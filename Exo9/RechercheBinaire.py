#IMPORT
import random

#FONCTIONS
def CréationTableau () :
    arr = []

    for i in range(500):
        arr.append(random.randrange(0,1000))

    arr.sort()

    return arr
    
def RechercheBinaire (arr,Debarr,Finarr) :
    elem = 42
    moitié = Debarr + (Finarr-Debarr)//2
      
    if Finarr >= Debarr : 
        if arr[moitié] > elem :    
            return RechercheBinaire(arr,Debarr,moitié-1)
            
        elif arr[moitié] < elem :
            return RechercheBinaire(arr,moitié+1,Finarr)

        elif arr[moitié] == elem :
            return moitié

    else :
        return "not find"

#MAIN
arr = CréationTableau()
rslt = RechercheBinaire(arr,0,len(arr)-1)

if rslt != "not find": 
     print (f"L'indice de 42 est {rslt}.")
else :
     print ("42 n'a pas été trouvé.")