
"""
Eleve POO

Ecrire une classe Eleve permettant 
d'instancier des étudiants.
Ils se carracterisent par 
un nom, un prenom, un age et une liste de notes.

L'eleve doit posseder au moins 2 methodes :
    - affichage(), permettant d'afficher ses informations.
    - moyenne(), permettant de calculer la moyenne de ses notes.

Il doit évidemment etre possible
de lui ajouter une note.
Il doit egalement etre possible 
de lui en supprimer une.
    
"""

class Eleve :
    
    def __init__(self,nom:str,prenom:str,age:int,list_notes: list) -> None:
        self.nom = nom 
        self.prenom = prenom 
        self.age = age
        self.list_notes = list_notes

    def affichage(self) :
        print(f"Informations de l'élève : \n - Nom : {self.nom} \n - Prénom : {self.prenom} \n - Age : {self.age} \n - Liste de notes : {self.list_notes} ")
    
    def moyenne(self) :
        moyenne = sum(self.list_notes) / len(self.list_notes)
        return moyenne
    
    def ajouter_note(self,note) :
        self.list_notes.append(note)
        
    def supprimer_note(self,liste,note) :
        for i in range (len(liste)):
            if liste[i] == note :
                index = i    
            
        self.list_notes.pop(index)
    
if __name__ == '__main__' :
    
    Said = Eleve('Cherifi','Said',31,[12,9,20,16,4])
    Said.affichage()
    print(Said.moyenne())
    Said.ajouter_note(20)
    Said.affichage()
    print(Said.moyenne())
    Said.supprimer_note(Said.list_notes,20)
    Said.affichage()
    print(Said.moyenne())

