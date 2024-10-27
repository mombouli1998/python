#! /usr/bin/env python3

#séquence àléatoire

import random

for i in range(6):
    print(random.randint(1,4))

#séquences aléatoires de bases
base=["A","C","G","T"]
sequence=[]

for i in range(20):
    t=random.choice(base)
    sequence.append(t)

print(sequence)