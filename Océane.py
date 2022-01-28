
import pygame as pg
from random import *

"variable SALLE: tableau numpy python"
"monstre=coordonnées de la position du monstre"

ESPACE_DISPO=[]

for i in range(len(SCREEN)):
    for j in range(len(SCREEN[0])):
        if SCREEN[i][j]=='.':
            ESPACE_DISPO.append((i,j))
    

personnage=random.choices(ESPACE_DISPO)
sac=[]
point_de_vie=5

a,b=personnage
personnage_new=(a+direction[0],b+direction[1]) 
message=''

if personnage_new in ESPACE_DISPO:

    if personnage_new in monstres:
        proba=[0,1]
        p=random.choices(proba)
        if p==0: 
            point_de_vie-=1
            message+='Vous avez rencontré un monstre, et vous avez perdu'
        if p==1:
            message+='Vous avez rencontré un monstre, et vous avez gagné'
            if point_de_vie!=5: 
                point_de_vie+=1

    if personnage_new in potions:
        if point_de_vie!=5:point_de_vie+=1
        else: sac.append(j)    

    personnage=personnage_new    

     








