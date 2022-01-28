
import pygame as pg
import random as rd

"variable SALLE: tableau numpy python"
"monstre=coordonnées de la position du monstre"




def espace_dispo(salle):
    ESPACE_DISPO=[]

    for i in range(len(salle)):
        for j in range(len(salle[0])):
            if salle[i][j]=='.':
                ESPACE_DISPO.append((i,j))
    return ESPACE_DISPO
    

def deplacement_personnage(personnage, direction, monstres, potions, points, salle, sac, étage):
    a, b = personnage
    ESPACE_DISPO = espace_dispo(salle)
    personnage_new = (a + direction[0], b + direction[1])

    message=''

    if personnage_new in ESPACE_DISPO:
        if personnage_new in monstres:
            monstres.remove(personnage_new)
            if étage == 0 or étage == 1:
                proba = [0, 1]
            elif étage == 2:
                proba = [0, 0, 1]
            elif étage == 3:
                proba = [0, 0, 0, 1]
            else:
                proba = [0, 0, 0, 0, 1]
            p = rd.choice(proba)
            if p == 0: 
                points -= 1
                message += 'Vous avez rencontré un monstre, et vous avez perdu'
            if p == 1:
                message += 'Vous avez rencontré un monstre, et vous avez gagné'
                if points < 10:
                    points += 1

        if personnage_new in potions:
            potions.remove(personnage_new)
            if points < 10:
                points += 1
            else: sac.append('potion')    
        personnage = personnage_new
    return personnage, points


def mouv_monstre(salle,personnage,coord_monstre):
    m1, m2 = coord_monstre
    p1, p2= personnage

    if m1<p1 and m2<p2:
        m1+=1
        m2+=1
    if m1<p1 and m2>p2:
        m1+=1
        m2-=1
    if m1>p1 and m2>p2:
        m1-=1
        m2-=1
    if m1>p1 and m2<p2:
        m1-=1
        m2+=1
    if m1==p1:
        if m2<p2:
            m2+=1
        else: m2-=1
    if m2==p2:
        if m1<p1:
            m1+=1
        else: m1-=1    

    return coord_monstre     


    
    

     







 


