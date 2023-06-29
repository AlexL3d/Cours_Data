

class IsbnValidator: 

    def vérifierIsbn(self, Isbn : int) -> bool:

        total = 0 

        for index in range(10):
            total += (Isbn%10) * (index+1)
            Isbn //= 10

        if total % 11 == 0:
            return True
        else :
            return False
