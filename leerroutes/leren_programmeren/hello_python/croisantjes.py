aantalCroissantjes = input("hoeveel croissantjes?:")
aantalCroissantjes = int(aantalCroissantjes)


totaalcroissantjes = aantalCroissantjes * 0.39
print(totaalcroissantjes, "euro")

aantalStokbroden = input("hoeveel stokbroden?:")
aantalStokbroden = int(aantalStokbroden)

totaalstokbroden = aantalStokbroden * 2.78
print(totaalstokbroden, "euro")


totaalprijs = totaalstokbroden + totaalcroissantjes - 1.50

print("‘De feestlunch kost je bij de bakker", totaalprijs ,"euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!’")



