# Import de defaultdict de la librairie collections
from collections import defaultdict


def WordCount(text):
    '''
    Fonction qui compte les mots dans un texte
    @param : du texte
    @return : dictionnaire  [clé : mot , valeur : son occurence]
    '''

    counts = defaultdict(int)
    for word in text.split():
        counts[word.lower()] += 1
    return counts

# ====================================================================================
# Modification en MapReduce de ce programme simple
# ====================================================================================


def map(valeur):
    '''
    Fonction qui transforme l'élément clé/valeur en liste d'éléments mot,occurence
    '''

    intermediaire = []
    for word in valeur.split():
        intermediaire.append((word.lower(), 1))

    return intermediaire


def reduce(key, valeurs):
    '''
    Fonction qui permet de fusionner les occurences de la liste des valeurs en une seule valeur
    '''
    valeur = 0
    for chaque_element in valeurs:
        valeur += chaque_element
    return (key, valeur)