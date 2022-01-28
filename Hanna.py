import random
from random import randint

def espace_dispo_point(salle):
    ESPACE_DISPO=[]

    for i in range(len(salle)):
        for j in range(len(salle[0])):
            if salle[i][j]=='.':
                ESPACE_DISPO.append((i,j))
    return ESPACE_DISPO


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
               for k in range(horizontal+1):
                   salle[x][y+k] = '-'
                   salle[x+vertical][y+k] = '-'
               for j in range(1, vertical):
                   salle[x+j][y] = '|'
                   salle [x+j][y+horizontal] = '|'
               for k in range(1, vertical):
                   for j in range(1, horizontal):
                       salle[x+k][y+j] = '.'
    return salle, recap_salles


def create_salle3(nb_lines, nb_columns, graal=False):
    salle = []
    recap_salles = []
    for i in range(nb_lines):
        salle += [[' ' for k in range(nb_columns)]]

    nb_salles = 15

    for numero in range(nb_salles):
        x,y = random.randint(2, nb_columns-2), random.randint(2, nb_lines-2)
        if salle[x][y] == ' ' and salle[x-1][y] == ' ' and salle[x][y-1] == ' ' and salle[x-1][y-1] == ' ' and 2<nb_lines-x-2 and    2<nb_columns-y-2:
            vertical = random.randint(2, nb_lines-x-2)
            horizontal = random.randint(2, nb_columns-y-2)
            if all([salle[x+l][y+i]==' ' for i in range(horizontal+2) for l in range(vertical+2)]):
                haut_gche = (x,y)
                bas_gche = (x + vertical,y)
                haut_drte = (x, y + horizontal)
                bas_drte = (x + vertical, y + horizontal)
                recap_salles.append([haut_gche, haut_drte, bas_gche, bas_drte])
                for k in range(horizontal+1) :
                    salle[x][y+k] = '-'
                    salle[x+vertical][y+k] = '-'
                for j in range(1, vertical) :
                    salle[x+j][y] = '|'
                    salle [x+j][y+horizontal] = '|'
                for k in range(1, vertical):
                    for j in range(1, horizontal):
                        salle[x+k][y+j] = '.'
    espacedispo = espace_dispo_point(salle)
    position_escalier = random.choice(espacedispo)
    salle[position_escalier[0]][position_escalier[1]] = '=' if not graal else 'g'
    for coordonnée in recap_salles :
        hg, hd, bg, bd = coordonnée[0], coordonnée[1], coordonnée[2], coordonnée[3]
        a, b, c, d = 0,0,0,0
        for k in range(hg[1], hd[1]):
            if a == 0 :
                for j in range(2, nb_lines - hg[0]-1):
                    if salle[hg[0]-j][k] == '-' or salle[hg[0]-j][k] == '|':
                        for l in range(-1, j+2):
                            salle[hg[0]-l][k]='#'
                        a+=1
                        break
        for k in range(hd[0], bd[0]):
            if b == 0 :
                for j in range(2, nb_columns - bd[1]-1):
                    if salle[k][bd[1]+j] == '-' or salle[k][bd[1]+j] == '|':
                        for l in range(-1, j+2):
                            salle[k][bd[1]+l] = '#'
                        b+=1
                        break
        for k in range(bg[1], bd[1]):
            if c == 0 : 
                for j in range(2, nb_lines - bg[0]-1):
                    if salle[bg[0]+j][k] == '-' or salle[bg[0]+j][k] == '|':
                        for l in range(-1, j+2):
                            salle[bg[0]+l][k]='#'
                        c+=1
                        break
        for k in range(hg[0], bg[0]):
            if d == 0 :
                for j in range(2, nb_columns - bg[1]-1):
                    if salle[k][bg[1]-j] =='-' or salle[k][bg[1]-j] =='|':
                        for l in range(-1, j+2):
                            salle[k][bg[1]-l] = '#'
                        d+=1
                        break
    return salle, recap_salles


def create_donjon(nb_lines, nb_columns):
    donjon = []
    for i in range(4):
        donjon.append(create_salle3(nb_lines, nb_columns)[0])

    donjon.append(create_salle3(nb_lines, nb_columns, True))
    return donjon
