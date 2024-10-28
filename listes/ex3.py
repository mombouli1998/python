#! /usr/bin/env python3

Sequence="TCTGTTAACCATCCACTTCG"
def complementaire(s):
    seq=str(s)
    seq2=list(seq)
    seq1=[]
    for i in seq2:
        if(i=="A"):
            seq1.append('T')
        if(i=="T"):
            seq1.append('A')
        if(i=="C"):
            seq1.append('G')
        if(i=="G"):
            seq1.append('C')
        seq1.reverse()
    return seq1
print(Sequence)
t=complementaire(Sequence)
print(t)
print()
#suppression des doublons
def delete_d(listes):
    lst=[]
    seq=[]
    for i in listes:
        lst.append(str(i))
    for i in lst:
        if(lst.count(i)>1):
            lst.remove(i)

    print(lst)
a=[5,1,1,2,5,6,3,4,4,4,2]
print(a)

delete_d(a)