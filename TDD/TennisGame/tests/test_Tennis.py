# import
from src.Tennis import Tennis
import unittest


class test_TennisGame(unittest.TestCase):

    def test_affichage_score_1(self):
        input = ""
        resultat = ("A 0 0 0 0 0 0 B 0 0 0 0 0 0")
        score = Tennis()
        test = score.affichage_score_jeu(input)
        self.assertEqual(resultat, test)

    def test_affichage_score_2(self):
        input = "A"
        resultat = ("A 0 0 0 0 0 15 B 0 0 0 0 0 0")
        score = Tennis()
        test = score.affichage_score_jeu(input)
        self.assertEqual(resultat, test)

    def test_affichage_score_3(self):
        input = "A,B,A,B,A"
        resultat = ("A 0 0 0 0 0 40 B 0 0 0 0 0 30")
        score = Tennis()
        test = score.affichage_score_jeu(input)
        self.assertEqual(resultat, test)


if __name__ == "__main__":
    unittest.main()
