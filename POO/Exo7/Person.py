from House      import House
from Apartment  import Apartment
from Porte      import Porte

class Person :
    
    def __init__(self,nom,surface,color) -> None:
        self.__nom = nom
        self.__logement = self.Choix(surface,color) 

    def Display(self,surface) :
        if surface > 50 :
            House.Display(self.GetLogement())
        else :
            Apartment.Display(self.GetLogement())

    def Choix(self,surface,color) :
        if surface > 50 :
            return House(surface,color)
        else : 
            return Apartment(surface,color)
     
    def GetLogement(self) :
        return self.__logement

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
        personne.Display(b)