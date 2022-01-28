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