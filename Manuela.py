from random import *

screen = ............
nb_lines = .........
nb_columns = ........

objets = [’B’, ’j’] #’*’, ’!’, ’(’, ’&’, ’o’

nb_monstres = random.randint(1, 3)
n = len(screen)

screen_objets = screen.copy()
monstres = []
potions = []


for i in range(nb_lines):
    for j in range(nb_columns):
        if screen[i][j] = ".":
            aleatoire = random.randint(1, 36)
            if aleatoire = 1:
                objet = random.choice(objets)
                screen_objets[i,j] = objet
                if objet == ’B’:
                    monstres.append((i,j))
                else:
                    potions.append((i,j))