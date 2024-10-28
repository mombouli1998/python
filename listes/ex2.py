#! /usr/bin/env pyhton3

#nombre de liste sans la methode sort
nombre=[8,3,12.5,45,25.5,52,1]


i=len(nombre)
while i!=0:
       t=min(nombre[:i])
       nombre.remove(t)
       nombre.append(t)
       i=i-1
print(nombre)

#séquence nucléique aléatoire
import random

def gen_seq_alea(n):
       base=["A","C","T","G"]
       x=int(n)
       sequence=[]
       sequence1=[]
       if(n%2==0):
            for i in range(x):
              o=random.choices(base,k=int(x/2))
              sequence.append(o)
            for i in sequence:
                 for u in i:
                      sequence1.append(u)
                 
       return sequence1
print(gen_seq_alea(16))
