"""
Dominos :

Creer une classe Domino qui permet d'instancier des dominos.

rappel : un domino a 2 coté, la face A et la face B.
sur chacune on y trouve des points en nombres de 0 à 6

un domino possede des methodes :
    - afficher() pour connaitre le score de ses faces
    - valeur() qui permet de calculer la valeur totale du domino.
"""
from random import randint

class Dominos :

    def __init__(self) -> None:
        self.points_face_A = randint(1,6)
        self.points_face_B = randint(1,6)

    def afficher (self) :
        print(f"La face A vaut {self.points_face_A} et la face B vaut {self.points_face_B}.")
        
    def valeur(self) :
        valeur_totale = self.points_face_A + self.points_face_B
        return valeur_totale
    
if __name__ == '__main__' :
    Dominos1 = Dominos()
    Dominos1.afficher()
    print(Dominos1.valeur())
        