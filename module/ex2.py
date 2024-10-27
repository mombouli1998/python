#! /usr/bin/env python3

#affichage des fichiers dansun repertoire courant sans la commande os.system
import os

print(os.listdir())

#affichage temporisé

import time

for i in range(10):
    print(i)
    time.sleep(1.0)