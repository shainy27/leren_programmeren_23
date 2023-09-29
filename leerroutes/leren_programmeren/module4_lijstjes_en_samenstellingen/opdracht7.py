from fruitmand import fruitmand
for naam in fruitmand:
    roundness = naam["round"]
    if roundness:
        print(naam["name"])