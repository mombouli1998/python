#! /usr/bin/env python3
#détermination des nombres premiers inférieux à 100

for i in range(2,100):
    cpt=0
    for y in range(1,i+1):
        z=i%y
        if(z==0):
            cpt=cpt+1
    if(cpt<=2):
        print(i, "est nombre premier")