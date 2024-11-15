#! /usr/bin/env python3

#récupération de toute les lignes contenant le mots Voyageur
import re
ligne=[]

with open('histoire.txt','r') as fichier:
    for file in fichier:
        if(re.search('voyageur',file) or re.search('Voyageur',file)):
            ligne.append(file)
print(ligne)
print()
#récupération des phrases contenu dans guillemets « » 
mots=re.compile('\s«\s([a-z]+\s[a-z]+\s)+»')

phrase=[]
with open('histoire.txt','r')as fichier:
    for file in fichier:
           phrase.append(file)
print(phrase[8])
d=phrase[8]
m=mots.search(" « vas tu jeune homme » demanda-t-elle.  je cherche arbre aux reves  ")
print(m.group(0))

#remplacement d'un caractère par un autre

mots=re.compile('homme')

with open('histoire.txt','r') as fichier, open('histoire1.txt','w') as fichier1:
     for file in fichier:
          ligne=mots.sub('femme',file)
          fichier1.write(ligne)
