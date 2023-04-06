def SelectionSort ():
    
    liste = [8 , 5 , 1 , 7 , 6 , 4]
    listetriée =[]
    print(liste)

    for index0 in range(len(liste)) :
        for index1 in range( index0 + 1 ,len(liste)) :
            if liste[index0] > liste[index1] :
              liste[index0], liste[index1] = liste[index1], liste[index0]
    
    print(liste)

SelectionSort()