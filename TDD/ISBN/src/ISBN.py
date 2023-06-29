

class IsbnValidator():

    def vérifierIsbn(self, Isbn):
        if len(Isbn) != 10:
            raise ValueError("Le code ISBN doit contenir 10 chiffres")
        elif list(Isbn) in [0,1,2,3,4,5,6,7,8,9,X]:
            raise ValueError("Le code ISBN doit contenir des chiffres ou X")
        else:

            total = 0
            Isbn_int = int(Isbn[:9])

            if Isbn[9] == "X":
                total += 10
            else:
                total += int(Isbn[9])

            for index in range(1, 10):
                total += (Isbn_int % 10) * (index+1)
                Isbn_int //= 10

            if total % 11 == 0:
                return True
            else:
                return False
