from Student import Student

def main () :

    try :
        étudiant = Student()
        print(étudiant.show())
        
    except TypeError as error :
        print(error)

main()