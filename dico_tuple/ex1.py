#! /usr/bin/env python3

#composition des aciddes aminés

acide="AGWPSGGASAGLAILWGASAIMPGALWA"
sequence={}
for i in acide:
    sequence[i]=acide.count(i)
print(sequence)
print()
#mots de deux lettres
mots={}
i=0
while i!=len(acide)-1:
    o=acide[i]+acide[i+1]
    mots[o]=acide.count(o)
    i=i+1
print(mots)