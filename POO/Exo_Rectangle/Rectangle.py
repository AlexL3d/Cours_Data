"""
Boite à chaussure POO

Ecrire une classe Boite à chaussure permettant 
de construire des Boite à chaussure
Ils se carracterisent par :
    - une longueur 
    - une largeur et
    - une haureur.

Un Boite à chaussure doit posseder 3 methodes :
    - affichage(), permettant d'afficher les informations du rectangle.
    - Surface(), permettant de calculer la surface du rectangle.
    - volume() de ma boite
"""


class Boite:

    def __init__(self, longueur, largeur, hauteur) -> None:
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur

    def affichage(self):
        print(
            f"Informations de la boîte : \n - Longueur : {self.longueur} \n - Largeur : {self.largeur} \n - Hauteur : {self.hauteur} \n - Surface : {self.surface()} \n - Volume : {self.volume()}")

    def surface(self):
        surface = self.longueur * self.largeur * 2 + self.longueur * \
            self.hauteur * 2 + self.largeur * self.hauteur * 2
        return surface

    def volume(self):
        volume = self.longueur * self.largeur * self.hauteur
        return volume


if __name__ == "__main__":
    boite = Boite(12, 5, 3)
    boite.affichage()
