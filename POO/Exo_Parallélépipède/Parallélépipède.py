"""
Rectangle POO

Ecrire une classe Rectangle permettant de construire des rectangles
Ils se carracterisent par une longueur et une largeur largeur.

Un Rectangle doit posseder 2 methodes :
    - Perimetre(), permettant de calculer le périmètre du rectangle.
    - Surface(), permettant de calculer la surface du rectangle.


Ecrire une classe fille Parallelepipede héritant de la classe Rectangle
Cette classe possede en plus un attribut hauteur
ainsi qu'une méthode Volume() permettant de calculer son volume.
"""

class Rectangle :

    def __init__(self,longueur,largeur) -> None:
        self.longueur = longueur
        self.largeur = largeur

    def Perimetre(self) :
        perimetre = self.largeur*2 + self.longueur*2
        return perimetre

    def Surface(self):
        surface = self.largeur * self.longueur
        return surface

class Parallelepipede(Rectangle):

    def __init__(self, longueur, largeur, hauteur) -> None:
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        volume = self.Surface() * self.hauteur
        return volume

if __name__ == '__main__' :
    Rec1 = Rectangle(12,5)
    print(Rec1.Perimetre())
    print(Rec1.Surface())
    
    Par1 = Parallelepipede(12,5,5)
    print(Par1.Perimetre())
    print(Par1.Surface())
    print (Par1.volume())
