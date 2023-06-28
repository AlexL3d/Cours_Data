

def Fizzbuzz(index:int)-> str:

    if (index % 3) == 0 and (index % 5 == 0):  # Si multiple de 3 et 5
        retour = "FizzBuzz"
    elif index % 3 == 0:  # Si multiple de 3
        retour = "Fizz"
    elif index % 5 == 0:  # Si multiple de 5
        retour = "Buzz"
    else:
        retour = str(index)

    return retour