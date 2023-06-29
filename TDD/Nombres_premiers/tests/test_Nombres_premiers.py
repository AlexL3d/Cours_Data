# import de la fonction Fizzbuzz
from src.Nombres_premiers import Nombres_Premiers
import pytest

# définition des tests pour la fonction Nombres_premiers


def test_Nombres_premiers_2():
    test = Nombres_Premiers(2)
    liste = [2]
    assert test == liste


def test_Nombres_premiers_8():
    test = Nombres_Premiers(8)
    liste = [2, 2, 2]
    assert test == liste

def test_Nombres_premiers_0():
    test = Nombres_Premiers(0)
    liste = []
    assert test == liste

def test_Nombres_premiers_1():
    test = Nombres_Premiers(1)
    liste = []
    assert test == liste

def test_Nombres_premiers_positifs():
    with pytest.raises(ValueError) as exception:
        Nombres_Premiers(-5)