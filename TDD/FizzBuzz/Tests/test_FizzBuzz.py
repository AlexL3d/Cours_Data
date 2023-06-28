# import de la fonction Fizzbuzz
from src.FizzBuzz import Fizzbuzz

# définition de la fonction FizzBuzz
def test_Fizzbuzz_9():
     # vérification de la valeur retournée par la fonction Fizzbuzz(9)
    test= Fizzbuzz(9)
    assert test == "Fizz"

def test_Fizzbuzz_10():
    # vérification de la valeur retournée par la fonction Fizzbuzz(10)
    test = Fizzbuzz(10)
    assert test == "Buzz"

def test_Fizzbuzz_15():
    # vérification de la valeur retournée par la fonction Fizzbuzz(15)
    test = Fizzbuzz(15)
    assert test == "FizzBuzz"

def test_Fizzbuzz_2():
    # vérification de la valeur retournée par la fonction Fizzbuzz(2)
    test = Fizzbuzz(2)
    assert test == "2"

def test_Fizzbuzz():
    # vérification de la valeur retournée par la fonction Fizzbuzz()
    test = ""
    for ind in range(1,101):
        test += Fizzbuzz(ind)
    assert test == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FizzBuzz3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344FizzBuzz4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FizzBuzz6162Fizz64BuzzFizz6768FizzBuzz71Fizz7374FizzBuzz7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FizzBuzz9192Fizz94BuzzFizz9798FizzBuzz" 
    