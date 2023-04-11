from Pokemon import Pokemon
from PokemonFeu import Pokemon_Feu
from PokemonEau import Pokemon_Eau
from PokemonPlante import Pokemon_Plante


class Test:

    def __init__(self) -> None:
        pass

    def Main(self):
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
        
        ratatac = Pokemon()
        ratatac.nom ="Ratatac"
        ratatac.atk = 80
        ratatac.hp = 100
        ratatac.AffichageStats()

        florizarre.Attaquer(dracaufeu)

        if dracaufeu.IsDead():
            print("Le pokémon attaqué est à terre !!!")
        else:
            print("Le pokémon attaqué est encore debout !")

#APPEL DES FONCTIONS
test = Test()
test.Main()