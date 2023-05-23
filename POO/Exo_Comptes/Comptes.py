"""
Compte Bancaire:

Ecrire une classe CompteBancaire qui représente un compte bancaire,
Il a pour attributs :
    - un numeroCompte (type numérique ) ,
    - un nom (nom du propriétaire du compte du type sting),
    - un solde.
Ce compte possede des methodes :
    - Versement() pour y ajouter de l'argent.
    - Retrait() pour y retirer de l'argent.
    - aficher() pour y afficher les details du compte.

Creer une class CompteRemuneree qui herite de CompteBancaire
Ce compte possede un taux d'interet.
ainsi qu'une methode pour les calculer et ajouter au compte.

"""


class Bancaire:

    def __init__(self, numcompte: int, nom: str, solde: int) -> None:
        self.NumeroDeCompte = numcompte
        self.nom = nom
        self.solde = solde

    def versement(self, somme):
        self.solde += somme

    def retrait(self, retrait):
        self.solde -= retrait

    def afficher(self):
        print(
            f"Détails du compte : \n - Titulaire : {self.nom} \n - Numéro de compte : {self.NumeroDeCompte} \n - Solde : {self.solde}")


class CompteRemuneree(Bancaire):

    def __init__(self, numcompte: int, nom: str, solde: int, taux: int) -> None:
        super().__init__(numcompte, nom, solde)
        self.tauxinteret = taux

    def calcultaux(self):
        self.solde += self.tauxinteret * self.solde


if __name__ == "__main__":
    compte1 = Bancaire(12340553123, "Leduc", 12000)
    compte1.versement(300)
    compte1.retrait(500)
    compte1.afficher()

    compte2 = CompteRemuneree(8583432423, "Delaire", 2000, 1.5)
    compte2.calcultaux()
    compte2.afficher()
