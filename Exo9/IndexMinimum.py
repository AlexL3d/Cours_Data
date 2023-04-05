#IMPORT
import random

#FONCTIONS
def CréationTableau () :
    arr = []

    for i in range(500):
        arr.append(random.randint(0,1000))
    return arr

def IndexMinimum() : 
    tab = CréationTableau ()
    nbr_min = tab[0]
    index_min = 0
    
    for index in range (1,len(tab)-1) :
        if  nbr_min > tab[index] :
            nbr_min = tab[index]
            index_min = index
    
    if index_min != 0 :
        tab[0] , tab[index_min] = tab[index_min] , tab[0]

    print(tab)
    print(f"L'index du plus petit nombre {tab[0]} vaut {index_min}.")       

#MAIN
IndexMinimum() 