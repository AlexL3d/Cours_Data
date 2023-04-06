
# définition de la classe
# class Voiture :
#     pass

# instanciation de classe : création d'un objet à partir de la classe
# fiat = Voiture()

# une classe possède des méthodes(fonctions) et des attributs (variables liées à l'objet)

# lors de la def d'une méthode dans une classe, le premier paramètre sera self (représente l'objet en lui-même)
class Voiture :

    def __init__(self) -> None: #appelée automatiquement quand on instancie une classe, c'est le constructeur
        self.marque = 'Peugeot'

    def démarrer(self):
        self.modele = '308'
        self.avancer()
            
    def avancer(self):
        print(self.marque,self.modele)

    def __str__(self) -> str: #méthode qui existe déjà, il suffit de les définir
        return "C'est une voiture"
    
class VoitureElectrique(Voiture) : #Classe héritage de voiture

    def démarrer(self) :
        super().démarrer()
        self.modele = "ion" #Redéfinition d'un attribut
        self.avancer()
        super().démarrer() + "avec le moteur électrique" #surcharge de méthode (appel d'une méthode de la classe + ajout )
        
    def avancer(self):
        print (self.modele)

voiture = Voiture()
voiture.démarrer()

voiture = VoitureElectrique()
voiture.démarrer()

