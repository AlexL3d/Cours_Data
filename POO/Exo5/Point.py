"""
Créez une classe appelée « Point ». 
Cette classe doit avoir 2 entiers (x, y) en tant que membres privés. 
Le constructeur doit définir les valeurs de x et y via des paramètres. 
La classe doit avoir une méthode publique appelée « distance ». 
Cela prend un seul paramètre(Point) et renvoie la distance entre les 2 points
"""

from random import randint
from math   import sqrt

class Point :

    def __init__(self) :
        x1,y1,x2,y2 = self.valeur()
        self.__x1 = x1
        self.__y1 = y1 
        self.__x2 = x2
        self.__y2 = y2 

    def __str__(self):
        return f"La distance entre x({self.__x1},{self.__y1})et y({self.__x2},{self.__y2}) est de {self.distance()}cm."

    def valeur(self) :
        nbr1 = randint(0,100)
        nbr2 = randint(0,100)
        nbr3 = randint(0,100)
        nbr4 = randint(0,100)
        return nbr1,nbr2,nbr3,nbr4
    
    def distance(self):
        return int(sqrt((self.__x1-self.__x2)**2 + (self.__y1-self.__y2)**2))

    @property
    def x1(self) :
        return self.__x1

    @x1.setter 
    def x1(self,valeur):
        self.__x1 = valeur

    @property
    def y1(self) :
        return self.__y1

    @y1.setter 
    def y1(self,valeur):
        self.__y1 = valeur

    @property
    def x2(self) :
        return self.__x2

    @x2.setter 
    def x2(self,valeur):
        self.__x2 = valeur

    @property
    def y2(self) :
        return self.__y2

    @y2.setter 
    def y2(self,valeur):
        self.__y2 = valeur