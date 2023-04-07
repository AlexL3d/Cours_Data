class Porte :

    def __init__(self,color) -> None:
        self.__color = color

    @property
    def color(self) :
        return self.__color

    @color.setter 
    def color(self,valeur):
        valeur = valeur.lower() #passage en minuscule
        couleurs =("rouge","verte","bleue","jaune","orange","violette","rose","gris")

        if valeur not in couleurs : 
            raise TypeError("Veuillez reseigner une couleur : ")
        self.__color = valeur

    def Display(self) : 
        print(f"je suis une porte, ma couleur est {self.__color}.")