#! /usr/bin/env pyhon3

hiver=["decembre","janvier","fevrier"]
printemp=["mars","avril","mai"]
ete=["juin","juillet","aout"]
automne=["septembre","octobre","novembre"]
saison=[hiver,printemp,ete,automne]

print(saison[2])
print(saison[1][0])
print(saison[1:2])
print(saison[:][1])

#table de 9
table=list(range(0,117,9))
print(table)
#nombre paire entre [2,10000] inclus
nombre=len(list(range(2,10002,2)))
print(nombre)