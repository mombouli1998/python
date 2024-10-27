#! /usr/bin/env python3

#conjecture de syracuse

n=100
s=[100]
i=0
while i<=100:
    if(n%2==0):
        n=int(n/2)
        i=i+1
        s.append(n)
    if(n%2!=0):
        n=(n*3)+1
        i=i+1
        s.append(n)
print(s)