# imports
from src.Isbn import IsbnValidator
import unittest

class test_IsbnValidator(unittest.TestCase):

    def test_IsbnValidator_valide(self):
        Isbn_Validator = IsbnValidator()
        resultat = Isbn_Validator.vérifierIsbn("1491926309")
        self.assertTrue(resultat,"Le numéro ISBN est valide")

    def test_IsbnValidator_invalide(self):
        Isbn_Validator = IsbnValidator()
        resultat = Isbn_Validator.vérifierIsbn("1491926308")
        self.assertFalse(resultat,"Le numéro ISBN est invalide")

    def test_IsbnValidator_valide_bis(self):
        Isbn_Validator = IsbnValidator()
        resultat = Isbn_Validator.vérifierIsbn("2100825208")
        self.assertTrue(resultat,"Le numéro ISBN est valide")

    def test_IsbnValidator_valide_tri(self):
        Isbn_Validator = IsbnValidator()
        resultat = Isbn_Validator.vérifierIsbn("043942089X")
        self.assertTrue(resultat,"Le numéro ISBN est valide")

    def test_IsbnValidator_nombre_Chiffre(self):
        Isbn_Validator = IsbnValidator()
        with self.assertRaises(ValueError):
            Isbn_Validator.vérifierIsbn("149192630")

if __name__ == "__main__":
    unittest.main()