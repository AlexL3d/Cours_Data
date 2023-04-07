from House      import House
from Apartment  import Apartment
from Porte      import Porte

class Person :
    
    def __init__(self,nom,surface,color) -> None:
        self.__nom = nom
        maison = House(surface)
        porte = Porte(color)
        self.Display(self.nom)

    def Display(self) :
        House.Display()
        Porte.Display()

    @property
    def nom(self) :
        return self.__nom

    @nom.setter 
    def nom(self,valeur):
        self.__nom = valeur
    
class Test :

    def __init__(self) -> None:
        pass

    def main (a,b,c) :
        personne = Person(a,b,c)
        personne.Display()

if __name__ == "__main__" :
    test = Test()
