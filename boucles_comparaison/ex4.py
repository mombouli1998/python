#! /usr/bin/env python3

#parcour de matrice
lig=[1,2,3,4]
col=[1,2,3,4]
for i in lig:
    for j in col:
        print("({},{})".format(i,j))
print()
#parcour de demi matrice
for i in lig:
    for j in col:
        if(i<j):
            print("({},{})".format(i,j))
     

    
print()