
def Thermométre(liste):

    if len(liste) == 0:
        temp = "0"

    elif len(liste) > 10000:
        raise ValueError("La liste contient trop de valeurs")

    else:
        temp = abs(liste[0])
        for index in range(1, len(liste)):
            
            if abs(liste[index]) - abs(temp) < 0 :
                temp = liste[index]
            elif abs(liste[index]) == abs(temp) :
                if temp < liste[index]:
                    temp = liste[index]

    return str(temp)
