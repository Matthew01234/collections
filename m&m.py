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




def sorteren (kleur1, kleur2):
  if dictonary[kleur1] > dictonary[kleur2]: return kleur1, kleur2
  else: return kleur2, kleur1

grotere1, kleinere1 = sorteren ('blauw', 'bruin')
grotere2, kleinere2 = sorteren ('oranje', 'groen')
nummer1, kleinere3 = sorteren (grotere1, grotere2)
grotere4, nummer4 = sorteren (kleinere1, kleinere2)
nummer2, nummer3 = sorteren(kleinere3, grotere4)
print('Groote aflopend: '+nummer1,nummer2,nummer3,nummer4)