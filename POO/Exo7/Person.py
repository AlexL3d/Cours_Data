from House      import House
from Apartment  import Apartment

class Person :
    
    def __init__(self,nom,surface,color) -> None:
        self.__nom = nom
        self.__logement = self.Choix(surface,color) 

    def Display(self) :
        pass

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
        personne.Display()

if __name__ == "__main__" :
    test = Test()