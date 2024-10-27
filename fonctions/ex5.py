#!/usr/bin/env python 3

#fonction distance à l'origine

import math
import random
def calc_distance2D(A,B):
    xA=A[0]
    yA=A[1]
    xB=B[0]
    yB=B[1]
    d=math.sqrt((math.pow((xB-xA),2)+math.pow((yA-yB),2)))
    return d
#calcul de la distance avec le point d'origine
def Calc_dist2ori(listx,listy):
        f=[]
        for i in range(len(listx)):
              b=[listx[i],listy[i]]
              a=[0,0]
              d=calc_distance2D(b,a)
              f.append(d)
        return f

#création  remplissage des la liste des  coordonnées de x
listx=[]
i=-math.pi
while i<=math.pi:
     listx.append(i)
     i=i+0.1
#création  remplissage des la liste des  coordonnées de x avec la fonction sin(x)
listy=[]
for i in listx:
     listy.append(math.sin(i))
#appelle de la fonction calc_dist2ori
fichier=Calc_dist2ori(listx,listy)

#creation et remplissage du fichier sin2ori.dat
with open('sin2ori.dat','w') as f:
      for i in range(len(fichier)):
            f.write(str(listx[i]))
            f.writelines(str(fichier[i])+"\n")
