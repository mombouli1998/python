#! /usr/bin/env python3

#fonction distance
import math

def calc_distance3D(A,B):
    xA=A[0]
    yA=A[1]
    zA=A[2]

    xB=B[0]
    yB=B[1]
    zB=B[2]

    d=math.sqrt((math.pow((xB-xA),2)+math.pow((yA-yB),2)+math.pow((yA-yB),2)))
    return d
A=[0,0,0]
B=[1,1,1]
print(math.sqrt(3))
print(calc_distance3D(A,B))