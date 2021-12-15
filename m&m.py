import random

def functie(aantal : int):
    zak = list()
    for x in range(aantal):
        mmkleur = (kleur[random.randint(0,3)])
        zak.append(mmkleur)

    return zak



kleur = ['oranje','blauw','groen','bruin']

aantal = int(input('Hoeveeel M&Ms wilt u?\n>>>')) 
zak = functie(aantal)
print(zak)





