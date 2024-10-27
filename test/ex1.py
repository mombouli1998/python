#! /usr/bin/env python3

#jour de de la semaine
semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

for i in range(len(semaine)):
    if(i<4):
        print(semaine[i],"au travaile")
    if(i==4):
        print("chouette c'est {}".format(semaine[i]))
    if(i>4):
        print("c'est le weekend {}".format(semaine[i]))
