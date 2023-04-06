"""
Écrivez une classe appelée « Student » avec les membres suivant :
    •nom (de type String),
    •note1, note2 (de type int)
Le programme demande à l’utilisateur d’entrer le nom et les notes. calc_moy() calcule la note 
moyenne et show() affiche le nom et la note moyenne
"""

class Student :

    def __init__(self) :
        n1, n2, n3 = self.saisie()
        self.set_n1(n1)
        self.set_n2(n2)
        self.set_n3(n3)
        
    def saisie(self) :
        n1 = input("Entrez un nom : ")
        n2 = int(input("Entrez un nombre : "))
        n3 = int(input("Entrez un nombre : "))
    
    def get_n2(self) :
            return self.__n2
    
    def set_n1(self,n1) :
        self.__n1 = n1
    
    def set_n2(self,n2) :
        if type(n2) == int or type(n2) == float :
            self.__n2 = n2
        else :
            raise TypeError("Il faut un nombre")
        
    def get_n3(self) :
        return self.__n3
    
    def set_n3(self,n3) :
        if type(n3) == int or type(n3) == float :
            self.__n3 = n3
        else :
            raise TypeError("Il faut un nombre")
        
    def moyenne(self) :
        return (self.__n2 + self.__n3)/2
        
    def show(self) :
        return f"La moyenne de {self.__n1} vaut {self.moyenne()}."