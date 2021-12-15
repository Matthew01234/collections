import random
mnmDictionaryBag = {}
oranje = 0
blauw = 0
bruin = 0
groen = 0

def functie(aantal : int):
    global mnmDictionaryBag, oranje, blauw, bruin, groen 
    oranje = 0
    blauw = 0
    bruin = 0 
    groen = 0
    zak = list()
    for x in range(aantal):
        mmkleur = (kleur[random.randint(0,3)])
        zak.append(mmkleur)
    for i in range (len(zak)):
        if zak[i] == 'oranje': 
            oranje += 1
        if zak[i] == 'blauw': 
            blauw += 1
        if zak[i] == 'bruin': 
            bruin += 1
        if zak[i] == 'groen': 
            groen += 1

    mnmDictionaryBag = { 

        'oranje' : oranje,
        'blauw' : blauw,
        'bruin' : bruin,
        'groen' : groen
    
    }
    return mnmDictionaryBag, 
 


kleur = ['oranje','blauw','groen','bruin']

aantal = int(input('Hoeveeel M&Ms wilt u?\n>>>')) 
zak = functie(aantal)

print (mnmDictionaryBag)
print ('oranje: '+ str(oranje) +'')
print ('blauw: '+ str(blauw) +'')
print ('bruin: '+ str(bruin) +'')
print ('groen: '+ str(groen) +'')
