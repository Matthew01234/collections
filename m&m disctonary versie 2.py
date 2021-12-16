import random
kleuren = ['oranje', 'groen', 'bruin', 'blauw']
dictonary = dict()

def MmMdictonary (aantal):
    global dictonary
    dictonary = {
        'groen' : 0,
        'oranje': 0,
        'bruin': 0,
        'blauw': 0
    }
    for i in range(aantal):
      gekozenkleur = random.choice(kleuren)  
      dictonary[gekozenkleur] += 1
    return dictonary

aantal = int(input ('Hoeveel moet er aan de zak toegevoegd worden?: '))
print(MmMdictonary(aantal))

def sorteren (kleur1, kleur2):
  if dictonary[kleur1] > dictonary[kleur2]: return kleur1, kleur2
  else: return kleur2, kleur1

grotere1, kleinere1 = sorteren ('blauw', 'bruin')
grotere2, kleinere2 = sorteren ('oranje', 'groen')
nummer1, kleinere3 = sorteren (grotere1, grotere2)
grotere4, nummer4 = sorteren (kleinere1, kleinere2)
nummer2, nummer3 = sorteren(kleinere3, grotere4)
print('Groote aflopend: '+nummer1,nummer2,nummer3,nummer4)