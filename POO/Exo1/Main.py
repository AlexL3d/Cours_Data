#Import du module
from Rectangle import Rectangle

#MAIN
try :
    ABCD = Rectangle("test",4)
    print(ABCD)
except TypeError as error : 
    print(error)