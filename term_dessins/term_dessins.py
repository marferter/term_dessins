def carre(longueur) :

    def cote(longueur) :
        forward(longueur)
        right(90)
        
    for _ in range(4) :
        cote(longueur)


def triangle(longueur) :

    def cote(longueur) :
        forward(longueur)
        right(120)

    for _ in range(3) :
        cote(longueur)
    
        