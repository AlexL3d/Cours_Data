""" Fichier de test pour la fonction `hello_world`.
"""

from MonModule1 import MaPartieA

def main():
    """ Une méthode pour dire bonjour à tout le monde.
    :return: None.

    """
    print("Hello World!")
    MaPartieA()


def main2():
    """ Une méthode pour tester un appel
    """
    print("Je suis importé")


if __name__ == "__main__":
    main()
else:
    main2()
