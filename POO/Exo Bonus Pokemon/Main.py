from Pokemon import Pokemon
from PokemonFeu import Pokemon_Feu
from PokemonEau import Pokemon_Eau
from PokemonPlante import Pokemon_Plante


class Test:

    def __init__(self) -> None:
        pass

    def Main(self):
        # Définition des stats des Pokemons
        dracaufeu = Pokemon_Feu()
        dracaufeu.nom = "Dracaufeu"
        dracaufeu.atk = 130
        dracaufeu.hp = 100
        dracaufeu.AffichageStats()

        tortank = Pokemon_Eau()
        tortank.nom = "Tortank"
        tortank.atk = 95
        tortank.hp = 180
        tortank.AffichageStats()

        florizarre = Pokemon_Plante()
        florizarre.nom = "Florizarre"
        florizarre.atk = 110
        florizarre.hp = 140
        florizarre.AffichageStats()

        ratattac = Pokemon()
        ratattac.nom = "Rattatac"
        ratattac.atk = 80
        ratattac.hp = 100
        ratattac.AffichageStats()


        # Début du combat
        dracaufeu.IsDead()
        florizarre.IsDead()

        while not dracaufeu.IsDead() and not florizarre.IsDead():
            florizarre.Attaquer(dracaufeu)
            dracaufeu.IsDead()
            
            if not dracaufeu.IsDead():
                dracaufeu.Attaquer(florizarre)
                florizarre.IsDead()

        if dracaufeu.IsDead():
            print("Dracaufeu a perdu !")
        elif florizarre.IsDead():
            print("Florizarre a perdu !")


# APPEL DES FONCTIONS
test = Test()
test.Main()
