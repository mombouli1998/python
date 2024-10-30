#! /usr/bin/env python3

#séquence nulceique aléatoire2
import random

def sequence(n):
    t=["A","T","C","G"]
    pond=[(n*(1/10)),(n*(1/10)),(n*(3/10)),(n*(5/10))]
    r=random.choices(t,weights=pond,k=n)
    print(r)

sequence(6)

#triangle de pascal

def pascal(n):
    x=int(n)
    t=[]
    for i in range(x):
        if(i==0):
            t.append("10")
        if(i>0):
            r=i-1
            u=t[r]
            c=u[0]
            y=0
            while y!=len(u)-1:
                a=int(u[y])
                b=int(u[y+1])
                d=a+b
                c=c+str(d)
                y=y+1
            c=c+"0"
            t.append(c)
    a=str(t[n-1])
    a=a.rstrip("0")        
    print(a)
pascal(4)