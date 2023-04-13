"""
– Créez une classe « Person »
– Créez une classe « Student » et une autre classe « Teacher », les deux héritent de la classe « Person ».
– La classe « Student » aura une méthode publique « GoToClasses », qui affichera à l’écran « I’m going
to class. ».
– La classe « Teacher » aura une méthode publique « Explain », qui affichera à l’écran « Explanation
begins ». En plus, il aura un attribut privé « subject » de type string.
– La classe « Person » doit avoir une méthode « SetAge(int n) » qui indiquera la valeur de leur âge (par 
exemple, 15 years old).
– La classe « Student » aura une méthode publique « DisplayAge » qui écrira sur l’écran « My age is: 
XX years old ».
– Vous devez créer une autre classe de test appelée « Test » qui contiendra « Main » et:
– Créez un objet Person et faites-lui dire « Hello »
– Créer un objet Student, définir son âge à 15 ans, faites-lui dire « Hello », « I’m going to class. » et 
afficher son âge
– Créez un objet Teacher, 40 ans, demandez-lui de dire « Hello » puis commence l’explication
"""


class Person:

    def __init__(self) -> None:
        pass

    def Hello(self):
        print("Hello!")

    def SetAge(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valeur):
        self.__age = valeur


class Student(Person):

    def __init__(self) -> None:
        super().__init__()

    def GoToClasses(self):
        print("I'm going to class")

    def DisplayAge(self):
        print(f"My age is : {self.age} years old")


class Teacher(Person):

    def __init__(self) -> None:
        super().__init__()
        self.__subject = "Coder Chat GPT"

    def Explain(self):
        print(f"Explanation begins : {self.subject}.")

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, valeur):
        self.__subject = valeur


class Test:

    def __init__(self) -> None:
        pass

    def main(self):

        personne = Person()
        personne.Hello()

        étudiant = Student()
        étudiant.Hello()
        étudiant.GoToClasses()
        étudiant.SetAge(15)
        étudiant.DisplayAge()

        prof = Teacher()
        prof.Hello()
        prof.SetAge(40)
        prof.Explain()
