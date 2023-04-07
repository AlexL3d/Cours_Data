from House import House
from Porte import Porte

class Person :
    
    def __init__(self,nom,surface,color) -> None:
        self.__nom = nom
        maison = House(surface)
        porte = Porte(color)
        self.Display(self.__nom)

    def Display(self) :

    @property
    def nom(self) :
        return self.__nom

    @nom.setter 
    def nom(self,valeur):
        self.__nom = valeur