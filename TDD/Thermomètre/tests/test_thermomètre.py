# import de la fonction Thermomètre
from src.Thermomètre import Thermométre
import random
import pytest


def test_thermométre_liste_1():
    list_therm = (2, 9, 1)
    test = Thermométre(list_therm)
    assert test == "1"


def test_thermomètre_liste_vide():
    list_therm = ()
    test = Thermométre(list_therm)
    assert test == "0"


def test_thermométre_liste_10000():
    list_therm = (range(10001))
    with pytest.raises(ValueError) as exception:
        Thermométre(list_therm)


def test_thermométre_liste_negatif():
    list_therm = [-19, 9, 5, -5]
    test = Thermométre(list_therm)
    assert test == "5"
