#! /usr/bin/env python3

#fonction pyramide

def pyramide(n):
    for i in range(1,n,2):
        print("{:^{}s}".format('x'*i,n))

pyramide(5)
print()

#fonction nombre premier

def is_prime(b):
    cpt=0
    for i in range(1,b+1):
        if(b%i==0):
            cpt=cpt+1
    if(cpt<=2):
        return True
    else:
        return False
i=2
while i<=20:
    print(i,is_prime(i))
    i=i+1