#!/usr/bin/env python3

#triangle
x="*"
for i in range(10):
    print(x*i)
print()
#triangle inversé
for i in range(10,0,-1):
    print(x*i)
print()
#triangle gauche
i=1
while i<10:
   
    print("{:^10s}".format(x*i))
    i=i+2