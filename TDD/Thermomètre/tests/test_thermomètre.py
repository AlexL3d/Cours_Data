# import de la fonction Thermomètre
from src.Thermomètre import Thermométre
import random


def test_thermométre_liste_1():
    list_therm = (2, 9, 1)
    test = Thermométre(list_therm)
    assert test == "1"


def test_thermomètre_liste_vide():
    list_therm = ()
    test = Thermométre(list_therm)
    assert test == "0"


def test_thermométre_liste_10000():
    list_therm = (random.random() for _ in range(10001))
    test = Thermométre(list_therm)
    with pytest.raises(ValueError) as exception:          
        assert str(exception.value) == "La liste contient trop de valeurs"


def test_thermométre_liste_negatif():
    list_therm = [-19, 9, 5, -5]
    test = Thermométre(list_therm)
    assert test == "5"
