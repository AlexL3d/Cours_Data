#FONCTIONS 

#Saisie du prix 
def Saisie() :
    
    prix = int(input("Entrez un prix hors taxe : "))

    while prix < 1 :
        prix = int(input("Entrez un prix hors taxe : "))

    taxe = input("Entrez un type de taxe (N/B) : ")

    while taxe != 'N' and taxe != 'B'  :
        taxe = input("Entrez un type de taxe (N/B) : ")
    return prix , taxe

#Calcul TTC
def TTC () :
    DicoTaxe = {"N":5.5,"B":20}
    ttc = 0

    prix , taxe = Saisie()

    for typ,value in DicoTaxe.items() :
        if typ == taxe :
            ttc = prix * (1 + ( value / 100 ) )
            print (f"{prix}€ avec {value}% de taxe, le prix est de {ttc}€.")

#MAIN
TTC ()