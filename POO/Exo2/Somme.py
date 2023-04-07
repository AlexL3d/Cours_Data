"""
Écrivez une classe « Somme » ayant deux variables « n1 » et « n2 » et une fonction membre « sum() » 
qui calcule la somme. Dans la méthode principale main demandez à l’utilisateur d’entrez deux entiers 
et passez-les au constructeur par défaut de la classe « Somme » et afficher le résultat de l’addition des 
deux nombres
"""

class Somme :
    
    def __init__(self):
        n1, n2 = self.saisie()
        self.set_n1(n1)
        self.set_n2(n2)

    def get_n1(self) :
        return self.__n1
    
    def set_n1(self,n1) :
        if type(n1) == int or type(n1) == float :
            self.__n1 = n1
        else :
            raise TypeError("Il faut un nombre")

    def get_n2(self) :
            return self.__n2
    
    def set_n2(self,n2) :
        if type(n2) == int or type(n2) == float :
            self.__n2 = n2
        else :
            raise TypeError("Il faut un nombre")

    def sum(self) : 
    
    def saisie(self):
        n1 = int(input("Entrez un nombre : "))
        n2 = int(input("Entrez un nombre : "))
        return n1,n2


    def __str__(self) :
        return f"La somme de {self.__n1} et {self.__n2} vaut {self.sum()}."