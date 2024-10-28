#! /usr/bin/env python3

#mots composable

def composable(a,b):
    x=str(a)
    y=str(b)
    t=True
    for i in x:
        w=int(x.count(i))
        z=int(y.count(i))
        if(w > 0 and w <=z):
           t=True
        else:
            t=False
    return t
      
print(composable("uocuoceokzefhu","coucou"))
print()


# alphabete pangramme
def get_alphabet():
    a=""
    for i in range(97,123):
        a=a+chr(i)
    return a

print(get_alphabet())
print()
#pangramme
def pangramme(a):
    x=str(a)
    y=x.replace(" ","")
    b=get_alphabet()
    d=composable(y,b)
    t=""
    
    if(d==True):
        print("{} / est un pangramme".format(x))
    if(d==False):
        print("{} / n'est un pangramme".format(x))

a="portez ce viux wisky au juge blond qui fume"
b="monsieur jack vous dactylographiez bien mieux que votre ami wolf"

c="je vais manger dupain"


pangramme(a)
pangramme(b)
pangramme(c)