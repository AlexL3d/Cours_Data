#FONCTIONS
def WordReverse() :
    phrase = "ceci n'est pas un poulet"
    affichage = ""
    tab=[]

    for index in range(len(phrase)) :
        if phrase[index] != ' ' :
            affichage += phrase[index] 
        else :
            tab.append(affichage)
            affichage =""

    tab.append(affichage)
    print(' '.join(tab))
    tab.reverse()
    print(' '.join(tab))

    for index in range(len(tab)) : 
        mot=list(tab[index])
        mot.reverse()
        tab[index] = ''.join(mot)
    print(' '.join(tab))

#MAIN
WordReverse()