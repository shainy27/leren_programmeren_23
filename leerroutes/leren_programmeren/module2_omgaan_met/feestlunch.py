aantalCroissantjes = input("hoeveel croissantjes?:")
aantalCroissantjes = int(aantalCroissantjes)


totaalcroissantjes = aantalCroissantjes * 39
print(totaalcroissantjes, "cent")

aantalStokbroden = input("hoeveel stokbroden?:")
aantalStokbroden = int(aantalStokbroden)

totaalstokbroden = aantalStokbroden * 278
print(totaalstokbroden, "cent")



totaalprijs = (totaalstokbroden + totaalcroissantjes - 150) / 100


print("‘De feestlunch kost je bij de bakker", totaalprijs ,"euro voor",aantalCroissantjes, "croissantjes en", aantalStokbroden, "stokbroden als de 3 kortingsbonnen nog geldig zijn!’")