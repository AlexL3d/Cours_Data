
class BowlingGame():
    
    def void_roll(nombre: int) -> int : 
        return nombre

    def party() -> list:
        
        liste = []
        for index in range(1,11):
            liste.append(index)
        return liste

    def manche(nb1,nb2) -> list:
        
        liste = []
        if nb1 != 10 :
            liste.append(BowlingGame.void_roll(nb1))
            liste.append(BowlingGame.void_roll(nb2))
        else : 
            liste.append(BowlingGame.void_roll(nb1))
            liste.append(0)
        
        return liste

    def int_score(liste : list) -> (int,str):

        coef = ""

        if sum(liste) == 10 :
            if liste[0] != 10:
                coef = "Spare"
            # else :
            #     coef = "Strike"
        return sum(liste),coef