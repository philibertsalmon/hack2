import random
from random import randint
import numpy as np
from Océane import espace_dispo

def create_salle(nb_lines, nb_columns):
    salle = []
    for i in range(nb_lines):
        salle += [[' ' for k in range(nb_columns)]]

    x,y = random.randint(1, nb_columns-2), random.randint(1, nb_lines-2)

    vertical = random.randint(2, nb_lines-y-1)
    horizontal = random.randint(2, nb_columns-x-1)
    for k in range(horizontal+1) :
        salle[x][y+k] = '-'
        salle[x+vertical][y+k] = '-'
    for j in range(1, vertical) :
        salle[x+j][y] = '|'
        salle [x+j][y+horizontal] = '|'
    for k in range(1, vertical):
        for j in range(1, horizontal):
            salle[x+k][y+j] = '.'
    return salle

def create_salle2(nb_lines, nb_columns):
   salle = []
   recap_salles = []
   for i in range(nb_lines):
       salle += [[' ' for k in range(nb_columns)]]

   nb_salles = 15

   for numero in range(nb_salles):
       x,y = random.randint(2, nb_columns-2), random.randint(2, nb_lines-2)
       if salle[x][y] == ' ' and salle[x-1][y] == ' ' and salle[x][y-1] == ' ' and salle[x-1][y-1] == ' ' and 2<nb_lines-x-2 and 2<nb_columns-y-2:
           vertical = random.randint(2, nb_lines-x-2)
           horizontal = random.randint(2, nb_columns-y-2)
           if all([salle[x+l][y+i]==' ' for i in range(horizontal+2) for l in range(vertical+2)]):
               haut_gche = (x,y)
               bas_gche = (x + vertical,y)
               haut_drte = (x, y + horizontal)
               bas_drte = (x + vertical, y + horizontal)
               recap_salles.append([haut_gche, bas_gche, haut_drte, bas_drte])
               for k in range(horizontal+1) :
                   salle[x][y+k] = '-'
                   salle[x+vertical][y+k] = '-'
               for j in range(1, vertical) :
                   salle[x+j][y] = '|'
                   salle [x+j][y+horizontal] = '|'
               for k in range(1, vertical):
                   for j in range(1, horizontal):
                       salle[x+k][y+j] = '.'
    return salle, recap_salles


def create_salle3(nb_lines, nb_columns):
   salle = []
   recap_salles = []
   for i in range(nb_lines):
       salle += [[' ' for k in range(nb_columns)]]

   nb_salles = 15

   for numero in range(nb_salles):
       x,y = random.randint(2, nb_columns-2), random.randint(2, nb_lines-2)
       if salle[x][y] == ' ' and salle[x-1][y] == ' ' and salle[x][y-1] == ' ' and salle[x-1][y-1] == ' ' and 2<nb_lines-x-2 and 2<nb_columns-y-2:
           vertical = random.randint(2, nb_lines-x-2)
           horizontal = random.randint(2, nb_columns-y-2)
           if all([salle[x+l][y+i]==' ' for i in range(horizontal+2) for l in range(vertical+2)]):
               haut_gche = (x,y)
               bas_gche = (x + vertical,y)
               haut_drte = (x, y + horizontal)
               bas_drte = (x + vertical, y + horizontal)
               recap_salles.append([haut_gche, bas_gche, haut_drte, bas_drte])
               for k in range(horizontal+1) :
                   salle[x][y+k] = '-'
                   salle[x+vertical][y+k] = '-'
               for j in range(1, vertical) :
                   salle[x+j][y] = '|'
                   salle [x+j][y+horizontal] = '|'
               for k in range(1, vertical):
                   for j in range(1, horizontal):
                       salle[x+k][y+j] = '.'
    espacedispo = espace_dispo(salle)
    position_escalier = random.choice(espacedispo)
    salle[position_escalier[0], position_escalier[1]] = '='
    return salle, recap_salles


def create_donjon(nb_lines, nb_columns):
    donjon = []
    for i in range(5):
        donjon.append(create_salle3(nb_lines, nb_columns)[0])
    return donjon