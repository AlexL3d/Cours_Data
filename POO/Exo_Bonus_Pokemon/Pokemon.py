"""
Contexte : 
Vous connaissez certainement tous ces petites bêtes toute mignonnes (ou pas pour certaines)
Ces petites créatures sont dressées par des "dresseurs de pokemons" et sont amenées à combattre entre elles.
Et bien, nous allons aussi les faire combattre !
Les Pokémon sont certes de très mignonnes créatures, mais ils sont également un bon exemple pour illustrer l’héritage. 

Je vous propose de commencer par créer une classe "Pokemon" qui contient les champs suivants : 
    ▪ un attribut nom qui représente le nom du Pokémon.
    ▪ un attribut hp (pour Health Points) qui représente les points de vie du Pokémon.
    ▪ un attribut qui s’appelle atk qui représente la force de base de l’attaque du Pokémon.
    ▪ un constructeur pour instancier des Pokémon adéquatement.
    ▪ une méthode isDead() qui retourne un boolean pour indiquer si un Pokémon est mort (hp == 0) ou non.

Créez une méthode "attaquer(Pokemon p)" qui permet au Pokémon appelant d’attaquer le Pokémon passé en paramètre. 
L’attaque déduit atk points de la vie hp du Pokémon attaqué p.
Redéfinissez la méthode toString() qui va nous permettre d'afficher  les informations du Pokémon.

En plus des Pokémon dit "normaux" (décrits à travers la classe Pokemon), on ressence trois types de Pokémon :
    ▪ Les Pokémon de type Feu
    ▪ Les Pokémon de type Eau
    ▪ Les Pokémon de type Plante 
(en réalité il existe 17 types en tout mais on ne va pas s’amuser à tous les coder)

les Pokémon de type Feu sont super efficaces contre les Pokémon de type Plante et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Feu et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

les Pokémon de type Eau sont super efficaces contre les Pokémon de type Feu et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Plante et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

les Pokémon de type Plante sont super efficaces contre les Pokémon de type Eau et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Plante ou de type Feu et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

Créez trois classes : 
    ▪ PokemonFeu
    ▪ PokemonEau
    ▪ PokemonPlante
Ces classes héritent de la classe Pokemon et qui représentent les trois types de Pokémon 
susmentionnés. 
Ensuite, amusez-vous à faire des combats de Pokémon.
"""


class Pokemon:

    def __init__(self) -> None:
        self.nom = None
        self.atk = None
        self.hp = None
        self.type = "Normal"

    def IsDead(self):
        pokemon_dead = False

        if self.hp <= 0:
            pokemon_dead = True

        return pokemon_dead

    def Attaquer(self, pokemon_attaqué):
        print(f"{self.nom} attaque {pokemon_attaqué.nom} !!!")

        self.TypAtk(pokemon_attaqué)
        pokemon_attaqué.hp = pokemon_attaqué.hp - self.atk

    def TypAtk(self, pokemon_attaqué):

        if self.type == "Feu":
            if pokemon_attaqué.type == "Eau":
                self.atk *= 1/2
            elif pokemon_attaqué.type == "Plante":
                self.atk *= 2
        elif self.type == "Eau":
            if pokemon_attaqué.type == "Plante":
                self.atk *= 1/2
            elif pokemon_attaqué.type == "Feu":
                self.atk *= 2
        elif self.type == "Plante":
            if pokemon_attaqué.type == "Feu":
                self.atk *= 1/2
            elif pokemon_attaqué.type == "Eau":
                self.atk *= 2

    def AffichageStats(self):
        print(
            f"Pokemon : {self.nom} / HP : {self.hp} / ATK : {self.atk} / TYPE : {self.type}")
