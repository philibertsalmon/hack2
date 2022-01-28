import pygame as pg
import random as rd

from Manuela import manu
from Hanna import create_salle, create_salle2
from Océane import *

pg.init() #on initialise pygame, une fois au début du programe

cell_size = 15
nb_lines = 30
nb_columns = 30

salle = create_salle2(nb_lines, nb_columns) # Nouvelle salle de Hanna
murs = []
espace_vide = []
portes = []
chemins = []
for i in range(nb_lines):
    for j in range(nb_columns):
        if salle[i][j] == '|' or salle[i][j] == '-':
            murs.append((i,j))
        elif salle[i][j] == '.':
            espace_vide.append((i,j))
        elif salle[i][j] == '+':
            portes.append((i,j))
        elif salle[i][j] == '#':
            chemins.append((i,j))

potions, monstres = manu(salle, nb_lines, nb_columns)


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
bleu = (0, 0, 255)
gris = (124, 124, 124)
jaune = (255, 255, 0)
violet = (238, 130, 238)
orange = (255, 128, 0)

DIR_ZERO = (0, 0)
DIR_LEFT = (-1, 0)
DIR_BOTTOM = (0, 1)
DIR_TOP = (0, -1)
DIR_RIGHT = (1, 0)

running = True


# Init :
personnage = rd.choice(espace_dispo(salle))
sac = []
points = 5
direction = DIR_ZERO

while running:

    screen = pg.display.set_mode((nb_lines*cell_size,nb_columns*cell_size)) # Fenêtre
    pg.display.set_caption(f'Rogue game --- points : {points}') # Titre fenêtre
    clock = pg.time.Clock()

    #On vérifie s'il est pas mort
    running = points > 0

    # Acquisition des flèches
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                direction = DIR_TOP
            elif event.key  == pg.K_DOWN:
                direction = DIR_BOTTOM
            elif event.key == pg.K_RIGHT:
                direction = DIR_RIGHT
            elif event.key == pg.K_LEFT:
                direction = DIR_LEFT
            break

    # Refresh perso :
    personnage, points = deplacement_personnage(personnage, direction, monstres, potions, points, salle, sac)
    direction = DIR_ZERO

    # Affichage de la salle
    screen.fill(black)
    # Les murs:
    for mur in murs:
        pg.draw.rect(
            screen,
            red, (mur[0] * cell_size,
            mur[1] * cell_size, cell_size, cell_size)
        )
    for porte in portes:
        pg.draw.rect(
            screen,
            bleu, (porte[0] * cell_size,
            porte[1] * cell_size, cell_size, cell_size)
        )  
    for espace in espace_vide:
        pg.draw.rect(
            screen,
            white, (espace[0] * cell_size,
            espace[1] * cell_size, cell_size, cell_size)
        )
    for chemin in chemins:
        pg.draw.rect(
            screen,
            gris, (chemin[0] * cell_size,
            chemin[1] * cell_size, cell_size, cell_size)
        )

    # Affichage des potions
    for potion in potions:
        pg.draw.rect(
            screen,
            jaune, (potion[0] * cell_size,
            potion[1] * cell_size, cell_size, cell_size)
        )

    # Affichage des monstres
    for monstre in monstres:
        pg.draw.rect(
            screen,
            violet, (monstre[0] * cell_size,
            monstre[1] * cell_size, cell_size, cell_size)
        )

    # Affichage du perso
    pg.draw.rect(
        screen,
        orange, (personnage[0] * cell_size,
        personnage[1] * cell_size, cell_size, cell_size)
    )

    # Affichage
    #to_print = 
    #font = pg.font.Font('freesansbold.ttf', 32)
    #text = font.render(to_print, True, black, white)



    pg.display.update()

# Il est mort :

for loop in range(10):
    clock.tick(10)
    screen.fill((255,255,0))
    pg.display.update()