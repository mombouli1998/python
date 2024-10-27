#! /usr/bin/env python3

#séquence complémentaire d'un brin d'adn
sequence=["A","C","G","T","T","A","G","G","C","T","A","A","C","G"]
comp=[]
for s in sequence:
    if(s=="A"):
        comp.append("T")
    if(s=="T"):
        comp.append("A")
    if(s=="G"):
        comp.append("C")
    if(s=="C"):
        comp.append("G")
print(sequence)
print(comp)
print()

#fréquence  des acides aminés
sequence=["A","R","A","W","R","W","W","G","A","G","A","W","R","G"]
s_A=0
s_R=0
s_G=0
s_W=0
print(sequence)
for s in sequence:
    if(s=="A"):
        s_A=s_A+((1/len(sequence))*100)
    if(s=="R"):
        s_R=s_R+((1/len(sequence))*100)
    if(s=="W"):
        s_W=s_W+((1/len(sequence))*100)
    if(s=="G"):
        s_G=s_G+((1/len(sequence))*100)

print("la fréquence de A est de {}".format(s_A))
print("la fréquence de R est de {}".format(s_R))
print("la fréquence de G est de {}".format(s_G))
print(" la fréquence de W est de {}".format(s_W))
print("le totale donne {}".format(s_A+s_G+s_R+s_W))