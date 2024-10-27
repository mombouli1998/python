#! /usr/bin/env python3

#jour de naissance
import calendar

jour=calendar.weekday(1998,2,24)

print(jour)

#0->lundi, 1->Mardi, 2->mercredi, 3->jeudi, 4->vendredi, 5->samedi 6->dimanche

#détermination du nombre pi pa la méthode de monte carlo
import random
import math

ns=0
N=10
r=1
for i in range(N):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    dx=math.pow(x-0,2)
    dy=math.pow(y-0,2)
    d=math.sqrt(dx+dy)
    if(d<1):
        ns=ns+1

pie=4*(ns/N)
print(pie)