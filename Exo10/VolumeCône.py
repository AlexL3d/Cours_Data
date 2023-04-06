import math

#Saisie des paramètres du cône
def Saisie() :
    rayon = float(input("Entrez le rayon du cône : "))

    while rayon <=0 :
        rayon = float(input("Entrez le rayon du cône : "))

    hauteur = float(input("Entrez la hauteur du cône : "))

    while hauteur <=0 :
        hauteur = float(input("Entrez la hauteur du cône : "))


    return rayon, hauteur

def CalulVolumeCône() :
    rayon, hauteur = Saisie()

    base = math.pi * rayon ** 2
    volume = base * hauteur / 3

    print("Le volume du cône, avec une hauteur de {}cm et un rayon de {}cm vaut {:0.02f}cm3.".format(hauteur,rayon,volume))

CalulVolumeCône()