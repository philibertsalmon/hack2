import random as rd
from turtle import pos

def manu(salle, nb_lines, nb_columns):
    objets = ["B", "j"] #"*", "!", "(", "&", "o"


    screen_objets = salle.copy()
    monstres = []
    potions = []


    for i in range(nb_lines):
        for j in range(nb_columns):
            if salle[i][j] == ".":
                aleatoire = rd.randint(1, 36)
                if aleatoire == 1:
                    objet = rd.choice(objets)
                    screen_objets[i,j] = objet
                    if objet == "B":
                        monstres.append((i,j))
                    else:
                        potions.append((i,j))
    return potions, monstres