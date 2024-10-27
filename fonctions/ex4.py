#! /usr/bin/env python3

#fonction distribution et stat
import random

def gen_distrib(debut,fin,n):
    nombre_reel=[]
    for i in range(n):
        nombre_reel.append(random.uniform(debut,fin))
    return nombre_reel

def calc_stat(n):
    listes=[]
    listes.append(min(n))
    listes.append(max(n))
    medianes=0
    moyenne=0
    
    m=int(len(n)/2)
    if(m%2==0):
         medianes=(n[m-1]+n[m])/2
    if(m%2!=0):
        medianes=n[m]
    for i in n:
        moyenne=moyenne+(i/len(n))
    listes.append(medianes)
    listes.append(moyenne)
    return listes

n=100
for i in range(1,21):
    nb=gen_distrib(0,100,n)
    nc=calc_stat(nb)
    print("List {} : min= {} ; max= {} ; mediane= {} ; moyenne= {} ".format(i,nc[0],nc[1],nc[2],nc[3]))