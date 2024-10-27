#! /usr/bin/envpython3

#nombres paires
for i in range(20):
    if(i%2==0 and i<=10):
        print("{} est paire et inférieur ou égale à 10".format(i))
    if(i%2!=0 and i>10):
        print("{} est impaire et strictement supérieur à 10".format(i))
print()

#enigme ddu père fouras
nombre=0
for i in range(100,200):
    t=str(i)
    if(t[0]==t[1] or t[0]==t[2] or t[1]==t[2]):
        a=int(t[0])
        b=int(t[1])
        c=int(t[2])
        d=a+b+c
        if(d==5 and i%2==0):
            print(i)           
            
