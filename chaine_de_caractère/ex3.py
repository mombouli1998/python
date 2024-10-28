#! /usr/bin/env python3

#distance de hamming

def haming(a,b):
    h=0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            h=h+i
    return h
a=["A","C","G","T","T","A","G","G","C","T","A","A","C","G"]
b=["A","T","G","T","C","A","A","T","C","A","G","G","T","T"]
print(haming(a,b))

#palindrome
t="Never odd or even"
def palindrome(r):
    i=str(r)
    d=i.lower()
    u=d.replace(" ","")
    z=int(len(u))
    t=""
    chaine1=u[-1:-z-1:-1]
    if(u==chaine1):
        t=u+" est un palindrome"
    else:
        t=u+" n'est un palindrome"
    return t
   
print(palindrome(t))