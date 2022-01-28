import random
from random import randint
import numpy as np

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
               x1 = x
               x2 = x + vertical
               y1 = y
               y2 = y + horizontal
               recap_salles.append([x1, x2, y1, y2])
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

