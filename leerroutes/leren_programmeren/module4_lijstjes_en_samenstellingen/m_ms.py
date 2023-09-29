import random

kleuren = ("Oranje", "Blauw", "Groen", "Bruin")   #tuple 
aantal = int(input("Hoeveel M&m's? "))
zak = []

for i in range(aantal):              
    zak.insert(0 , random.choice(kleuren))

print(zak)


