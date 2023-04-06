"""
Écrivez une classe « Rectangle » ayant deux variables « a » et « b » et une fonction membre 
« surface() » qui retournera la surface du rectangle.
"""

class Rectangle:

    def __init__(self,longueur,largeur) -> None:
        self.set_longueur(longueur)
        self.set_largeur(largeur)

    def get_longueur(self) :
        return self.__longueur
    
    def set_longueur(self,valeur) :
        if type(valeur) == int or type(valeur) == float :
            self.__longueur = valeur
        else : 
            raise TypeError("Il faut un nombre.")

    # Autre écriture
    # @property
    # def longueur(self) :
    #     return self.__longueur

    # @longueur.setter
    # def longueur(self,valeur) :
    #     self.__longueur = valeur

    def get_largeur(self) :
        return self.__largeur
    
    def set_largeur(self,valeur) :
        if type(valeur) == int or type(valeur) == float :
            self.__largeur = valeur
        else : 
            raise TypeError("Il faut un nombre.")
    
    def Aire(self) : 
        return self.__longueur * self.__largeur
    
    def __str__(self) -> str:
        return f"L'aire du rectangle vaut {self.Aire()} pour la longueur {self.__longueur} et la largueur {self.__largeur}."