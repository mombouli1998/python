#!/usr/bin/env python3

#crétion d'un liste  paire
impaire=[1,3,5,7,9,11,13,15,17,19,21]
paire=[]
for i in impaire:
    paire.append(i+1)
print(paire)

#calcul de la moyenne
notes=[14,9,6,8,12]
moyenne=0
for i in notes:
    moyenne=moyenne+(i/len(notes))
print(moyenne)
print()
#produit de nombres consécutis
for i in range(12):
    print(i*(i+1))