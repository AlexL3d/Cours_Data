
class Tennis() :

    def affichage_score_jeu(self, entrée):
        liste = entrée.split(",")
        listeA=[0,0,0,0,0,0]
        listeB=[0,0,0,0,0,0]

        for index in range(len(liste)):
            if liste[index] == "A":
                if listeA[index-1] != 30:
                    listeA[index-1] += 15
                else:
                    listeA[index-1] += 10
            elif liste[index] == "B":
                if listeA[index-1] != 30:
                    listeA[index-1] += 15
                else:
                    listeA[index-1] += 10


        output = ' '.join("A" + listeA + "B" + listeB)
        return output