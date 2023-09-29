from fruitmand import fruitmand
fruitmand = sorted(fruitmand , key = lambda fruit:fruit['weight'], reverse=True)     #sorteerd de fruitmand op gewicht
for fruit in fruitmand:
        print(fruit['name'],fruit['weight'])