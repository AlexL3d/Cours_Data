# imports
from src.ISBN import IsbnValidator
import unittest

class test_IsbnValidator(unittest.TestCase):

    def test_IsbnValidator_valide(self):
        IsbnValidator = IsbnValidator()
        resultat = IsbnValidator.vérifierIsbn(1491926309)
        self.assertTrue(resultat,"Le numéro ISBN est valide")

    def test_IsbnValidator_invalide(self):
        IsbnValidator = IsbnValidator()
        resultat = IsbnValidator.vérifierIsbn(1491926308)
        self.assertFalse(resultat,"Le numéro ISBN est invalide")

    def test_IsbnValidator_validebis(self):
        IsbnValidator = IsbnValidator()
        resultat = IsbnValidator.vérifierIsbn(2100825208)
        self.assertTrue(resultat,"Le numéro ISBN est valide")

if __name__ == "__main__":
    unittest.main()