print("bienvenue dans le programme de gestion de salaire")
nom=input("donnez votre nom") 


def repartition():
    salaire =int(input("entrer votre salaire "))
    essentiel=salaire*0.50
    print("les besions  essentiel s'elevent a:",essentiel," fcfa")
    inves=salaire*0.20
    print("les besion de l'investisement s'elevent a:",inves,"fcfa")
    epargne=salaire*0.20
    print("les besion des épargne s'elevent a:",epargne,"fcfa ")
    loisir=salaire*.10
    print("les besion des loisirs s'elevent a",loisir,"fcfa")
    
    return True

repartition()
