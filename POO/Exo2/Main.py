from Somme      import Somme

def main () :
    try :
        somme = Somme()
        print(somme)
    except TypeError as error :
        print(error)

main()