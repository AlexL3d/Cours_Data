#FONCTIONS

def Saisie () :
    liste =[]
    tailleliste = int(input("Entrez la taille de votre liste : "))

    for index in range (tailleliste) :
        liste.append(int(input("Entrez un chiffre : ")))

    return liste

def BubbleSort () :
    liste=Saisie()
    booleen = False

    print(liste)

    while booleen == False :
        booleen = True
        for index in range (len(liste)-1) :
            if liste[index] > liste[index+1] :
                liste[index], liste[index+1] = liste[index+1], liste[index]
                booleen = False 
    
    print(liste)

#MAIN 
BubbleSort()
