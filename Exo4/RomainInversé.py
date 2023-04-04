#FONCTIONS
def listeRomainInversé () :
    chiffreRomain = 'CMXCIX'
    chiffreArabe = 0
    stockage = ""
    booleen = False
    DicoRomain = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
    
    for index in range(len(chiffreRomain)-1) :
        if DicoRomain[chiffreRomain[index]] < DicoRomain[chiffreRomain[index+1]] :
            stockage = ""
            stockage += chiffreRomain[index]
            stockage += chiffreRomain[index+1]
            chiffreArabe += DicoRomain[stockage]
            booleen = True
        else :
            if booleen == False :
                chiffreArabe += DicoRomain[chiffreRomain[index]]
            booleen = False

    print(f"Le nombre {chiffreRomain} en chiffres arabes s'écrit : {chiffreArabe}.")

#MAIN==================================
listeRomainInversé()