#! /usr/bin/env python3
# minimum d'une liste
liste=[8,4,6,1,5]
mine=1000000
for i in liste:
    if(mine>i):
        mine=i
print(mine)
print()

#notes et mention d'un étudiant
notes=[14,9,13,15,12]
maxe=0
mines=21
moyenne=0
for i in notes:
    if(maxe<i):
        maxe=i
    if(mines>i):
        mines=i
    moyenne=moyenne+(i/len(notes))
print(maxe)
print(mines)
if(moyenne >=10 and moyenne <12 ):
    print("passable")
if(moyenne >=12 and moyenne<14):
    print("assez-bien")
if(moyenne >14):
    print("bine")
print(moyenne)

