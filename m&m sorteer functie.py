import random
kleuren = ['oranje', 'groen', 'bruin', 'blauw']

dictonary = {
        'groen' : 0,
        'oranje': 0,
        'bruin': 0,
        'blauw': 0
    }

lst = []

aantal = int(input ('Hoeveel moet er aan de zak toegevoegd worden?: '))

def toevoegen():
    global dictonary
    for i in range(aantal):
      gekozenkleur = random.choice(kleuren)  
      dictonary[gekozenkleur] = dictonary[gekozenkleur] + 1
    for i in range(aantal):
       gekozenkleur = random.choice(kleuren)
       lst.append(gekozenkleur)



def sorteren(sortVar):
    global dictonary
    if type(sortVar) == dict:
       sortVar = {k: v for k, v in sorted(sortVar.items(), key=lambda item: item[1], reverse=True)}
       print(sortVar)
       print ('gesorteerd op aantal')
    elif type(sortVar) == list:
        sortVar.sort()
        print(sortVar)
        print ('gesorteerd op alfabetische volgorde')

toevoegen()
sorteren(lst)

