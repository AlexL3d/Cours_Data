#FONCTIONS ===========================
#Saisie du nombre
def Saisie() -> int :
    entrée = int(input("Entrez un nombre entre 1 et 3999 : "))

    while entrée < 1 & entrée > 3999 :
        entrée = int(input("Entrez un nombre entre 1 et 3999 : "))
    return entrée

def listeRomain () :

    nombre = Saisie()
    nombre0 = nombre
    affichage = ""
    cpt = 0 

    DicoRomain = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
    
    for clé,valeur in DicoRomain.items() :
        while nombre >= valeur :
            cpt = nombre // valeur
            affichage += cpt * clé
            nombre -= cpt * valeur

    print(f"Le nombre {nombre0} en chiffres Romains s'écrit : {affichage}.")

#MAIN==================================
listeRomain()