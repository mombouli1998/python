#! /usr/bin/env python3
#numpy
import numpy as np

#création de matrice
matrice1=np.arange(10,0,-1)
print(matrice1)
print()
matrice1=np.array([[1,2,3],[2,5,7]])
print(matrice1)
print()
print("matrice1*matrice1 = \n",matrice1*matrice1,'\n')
print("matrice1*5 =\n",matrice1*5,"\n")
print("shape = ",matrice1.shape)
c=matrice1.reshape((3,2))
print("\n reshape(3,2)= \n",c)

matrice1.resize((1,6))
print("\nresize((1,6)) = \n ",matrice1)
print("\n matrice1[:] = ",matrice1[:])
print("\n matrice[0][::2] = ",matrice1[0][::2])
print("\n fonction zeros\n",np.zeros((3,3),int))
print("\n fonction ones = \n",np.ones((5,5),int))
print("\n fonction full =\n",np.full((6,6),7,int))
t=np.array([[1,2],[5,6]])
print("\n transposer d'une matrice =\n",np.transpose(t))
print("\n multiplication de matrice fonction dot =\n",np.dot(t,t))
print("\nfonction inv =\n",np.linalg.inv(t))
print("\n déterminant d'unen matrice =\n",np.linalg.det(t))

# matplotlib.pyplot
import matplotlib.pyplot as plot
#graphique 1
sequence1="LSEHGIOZEVIHJFZPOMJUVAOPZHEBNVNKJOOPZBJKJKEJKJKAJKSDBVKZHFMHIRGBVBJQSNJKQSLKAOIGAKEGJZEBGAAZEUGHBJQSGKAZ"
base=[]
occurance=[]
baseS={}
for s in sequence1:
    baseS[s]=sequence1.count(s)
for k,v in baseS.items():
    base.append(k)
    occurance.append(v)

base.sort()
plot.scatter(base,occurance,marker='o',color='blue')
plot.xlabel("base")
plot.ylabel("occurence")
plot.title("lettre et leur nombre d\'occurence")
plot.grid()
plot.savefig("graphique.pdf",bbox_inches='tight',dpi=200)

#graphique2
plot.scatter(base,occurance,marker='o',color='blue')
plot.xlabel("lettre")
plot.ylabel("occurence")
plot.title("lettre et leur nombre d\'occurence")
plot.plot(base,occurance,color='blue',ls='-')
plot.grid()
plot.savefig("graphique1.pdf",bbox_inches='tight',dpi=200)

#graphique3
x=np.arange(len(base))
plot.bar(x,occurance)
plot.xticks(x,base)
plot.xlabel("lettre")
plot.ylabel("occurence")
plot.title("lettre et leur nombre d\'occurence")
plot.grid()
plot.savefig("graphique2.pdf",bbox_inches='tight',dpi=200)