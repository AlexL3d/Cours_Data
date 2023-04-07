from House import House
from Porte import Porte

class Apartment(House) :
    def __init__(self,color) -> None:
        self.__surface = 50
        self.__porte = Porte(color)