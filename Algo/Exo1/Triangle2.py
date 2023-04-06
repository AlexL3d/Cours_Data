#FONCTIONS 

def Triangle () :
    for index in range (6) :
        print (('*' * index))

def TriangleInversé () :
    Triangle()
    for index in range (4,0,-1) :
        print (('*' * index))

#MAIN 

TriangleInversé()