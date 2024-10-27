#! /usr/bin/env python3

#fonction complement
direct=['A','T','C','G','A','T','C','G','A','T','C','G','C','T','G','C','T','A','G','C']
print(direct)

def complementaire(brin):
    compl=[]
    for i in brin:
        if(i=='A'):
            compl.append('T')
        if(i=='T'):
            compl.append('A')
        if(i=='C'):
            compl.append('G')
        if(i=='G'):
            compl.append('C')
    return compl
compl=complementaire(direct)
print(compl)
brin_direct="5 \'-"
brin_complementaire="3 \'-"

for i in range(len(direct)):
    if(i!=len(direct)-1):
        brin_direct=brin_direct+direct[i]
        brin_complementaire=brin_complementaire+compl[i]
    if(i==len(direct)-1):
        brin_direct=brin_direct+direct[i]+"-3\'"
        brin_complementaire=brin_complementaire+compl[i]+"-5\'"
print("brin direct : {}".format(brin_direct))
print("brin_complementaire : {}".format(brin_complementaire))