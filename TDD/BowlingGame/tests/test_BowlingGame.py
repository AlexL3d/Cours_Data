# imports
from src.BowlingGame import BowlingGame
import pytest
import random


def test_void_roll_5():
    test = BowlingGame.void_roll(5)
    assert test == 5

def test_10_void_roll() :
    résultat = [1,2,3,4,5,6,7,8,9,10]
    test = BowlingGame.party()
    assert test == résultat

def test_manche_2_5():
    résultat = [2,5]
    test = BowlingGame.manche(2,5)
    assert test == résultat

def test_manche_10():
    résultat = [10,0]
    test = BowlingGame.manche(10,0)
    assert test == résultat

def test_manche_suivante():
    résultat = 15
    liste_test = [5,5]
    test1,coef = BowlingGame.int_score(liste_test)
    if coef == "Spare":
        test2,coef = BowlingGame.int_score([liste_test[0]*2,liste_test[1]])
    else : 
        test2,coef = BowlingGame.int_score(liste_test)
    assert test2 == résultat