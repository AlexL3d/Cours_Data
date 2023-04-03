def Saisie():
    nom1, nom2, nom3 = input("Entrez trois noms séparés par un espace : ").split(" ")

    return nom1, nom2, nom3

def Controle() :

    nom1, nom2, nom3 = Saisie()

    if nom1 < nom2 < nom3 :
        print ("Les noms sont rangés dans l'ordre alphabétique.")
    else :
        print ("Les noms ne sont pas triés par ordre alphabétique.")
    
    return nom1, nom2, nom3

def Tri() :
    nom1, nom2, nom3 = Controle()
    tri = []
    tri.append(nom1)
    tri.append(nom2)
    tri.append(nom3)
    tri.sort()
    # Affichage avec la virgule
    tri = ', '.join(tri)
    print(f"Une fois trié, cela va donner : "+tri)

Tri()
