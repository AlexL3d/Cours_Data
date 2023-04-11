from House import House
from Porte import Porte

class Apartment(House) :
    def __init__(self,surface,color) -> None:
        super().__init__(surface, color)
        self.__surface = surface
        self.__porte = Porte(color)

    def Display(self) :
        print(f"Je suis un appartement, ma surface est de {self.surface} m².") 
        Porte.Display(self.GetDoor())

    def GetDoor(self) :
        return self.__porte