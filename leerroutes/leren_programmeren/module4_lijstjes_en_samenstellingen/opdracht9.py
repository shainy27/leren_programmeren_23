from fruitmand import fruitmand
for druif in range(len(fruitmand)):
    if fruitmand[druif]['name'] == 'druif':
        del fruitmand[druif]
        break
for fruit in fruitmand:
    print(fruit["color"])