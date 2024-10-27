#! /usr/bin/env python3

poly_a='A'
print(poly_a*20)

poly_GC='GC'
print(poly_GC*40)

# écriture formater
print("{} {} {}".format("salut",102,10.318))

propgc=((4500+2575)/14800)*100
print("le pourcentage de GC est {:.0f} %".format(propgc))
print("le pourcentage de GC est {:.1f} %".format(propgc))
print("le pourcentage de GC est {:.2f} %".format(propgc))
print("le pourcentage de GC est {:.3f} %".format(propgc))
print("le pourcentage de GC est {:.4f} %".format(propgc))