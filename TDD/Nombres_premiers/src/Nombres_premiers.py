def Nombres_Premiers(nombre):

    liste = []

    if nombre == 0 :
        pass

    elif nombre < 0 : 
        raise ValueError("Le nombre doit être positif")
        
    else :

        while nombre != 1:
            Boolean = True
            index = 2

            while ((Boolean == True) and (index <= nombre)):
                if nombre % index == 0:
                    liste.append(index)
                    nombre = nombre / index
                    Boolean = False
                index += 1

    return liste

if __name__ == '__main__':
    print(Nombres_Premiers(int(input("Entrez un nombre : "))))
