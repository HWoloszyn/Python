# -*- coding: utf-8 -*-

import random

lista1 = ["słowo", "lista", "papier", "kamień", "nożyce"]
lista2 = ["to", "jak", "i", "oraz", "lub"]
krotka = ("książka", "python", "komputer", "myszka", "test")


rand1 = random.randint(0,len(lista1)-1)
rand2 = random.randint(0,len(lista2)-1)
rand3 = random.randint(0,len(krotka)-1)


zdanie = lista1[rand1].capitalize() +" "+ lista2[rand2] +" "+ krotka[rand3] + ". (indeksy: " + str(rand1) + ", " + str(rand2) + ", " + str(rand3) + ")"
print (zdanie)

