from fruitmand import fruitmand
watermeloen = {'name' : 'watermeloen',
'weight' : 2000,
'color' : 'green',
'round' : True}
fruitmand.append(watermeloen)
gewicht1=0
for naam in fruitmand:
    gewicht = naam["weight"]
    gewicht1+=gewicht


print(gewicht1)