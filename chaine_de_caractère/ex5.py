#! /usr/bin/env python3

#affichage des carbones alpha d'unestructure de proteine
def trouve_alpha(alpha):
    x=str(alpha)
    liste_apha=[]
    with open(x,'r') as fichier:
        for i in fichier:
            file=i
            if(file.count("ATOM")>0 and file.count("CA")>0):
                liste_apha.append(file)
    return liste_apha

t='1bta.pdb'

proteine=trouve_alpha(t)

#calul des distance entre les carbonnes consécutifs d'une structure de proteine
#valeur de x est comprise entre les caractères 31 à 38
#valeur de y est comprise entre les caractères 31 à 38
#valeur de z est comprise entre les caractères 31 à 38

import  math

def calc_distance3D(A,B):
    xA=A[0]
    yA=A[1]
    zA=A[2]

    xB=B[0]
    yB=B[1]
    zB=B[2]

    d=math.sqrt((math.pow((xB-xA),2)+math.pow((yA-yB),2)+math.pow((yA-yB),2)))
    return d

def calcul_distance(lists):
    
    for i in range(len(lists)):
        if(i<len(lists)-1):
            z=lists[i]
            y=lists[int(i+1)]

            xA=float(z[31:38])
            yA=float(z[39:46])
            zA=float(z[47:54])
            A=[xA,yA, zA]

            xB=float(y[31:38])
            yB=float(y[39:46])
            zB=float(y[47:54])
            B=[xB,yB,zB]

            d=calc_distance3D(A,B)

            print("{} {} {:.2f}".format(i,i+1,d))
            
calcul_distance(proteine)