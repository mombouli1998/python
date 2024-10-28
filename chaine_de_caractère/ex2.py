#! /usr/bin/env python3

#parcours d'uneliste de chaines de caractères
animaux=['girafe','tigre','singe','souris']
for animal in animaux:
    print("{} de taille : {}".format(animal,len(animal)))

#fréquence des bases dans une séquence nucleique

def calc_composition(A):
    lst=[]
    lst.append((A.count('A')/len(A))*100)
    lst.append((A.count('C')/len(A))*100)
    lst.append((A.count('T')/len(A))*100)
    lst.append((A.count('G')/len(A))*100)
    return lst
     
sequence=["A","C","G","T","T","A","G","G","C","T","A","A","C","G"]
print(calc_composition(sequence))
