import random

kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']
zak = {}
aantal = int(input("Hoeveel M&M's wilt u in de zak doen? "))

for mm in range(aantal):
    kleur = random.choice(kleuren)
    if kleur in zak:
        zak[kleur]+=1
    else:
        zak[kleur]=1

print(zak)