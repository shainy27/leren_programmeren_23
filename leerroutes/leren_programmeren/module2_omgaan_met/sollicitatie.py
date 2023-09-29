

from ast import Name


naam = input("Wat is uw naam?")
if naam == "suhaly":
  raise NameError("Suhaly is hier niet welkom")

age = int(input("Hoe oud bent u?"))
if age == 36:
  raise NameError("u bent al veel te oud")

man = input("Bent u een man en heeft u een snor langer dan 10 cm? Ja/Nee")
if man == "ja":
  sollicitatie = True
else:
    vrouw = input("Bent u een vrouw met rood krulhaar van 20 cm? Ja/Nee")
    if vrouw == "ja":
     sollicitatie = True
    else:
      sollicitatie = False
  


ervaring = int(input("Hoeveel jaar praktijkervaring heeft u met dierendressuur"))
if ervaring >4:
  heeft_ervaring = True
else:
    ervaring = int(input("Hoeveel jaren ervaring heeft u met..."))
    if ervaring >4:
     heeft_ervaring = True
    else: 
      ervaring = int(input("hoeveel jaren ervaring heeft u met..."))
      if ervaring >5:
        heeft_ervaring = True
      else:
        heeft_ervaring = False


diploma = input("Bent u in bezit van een diploma MBO4 ondernemen? Ja/Nee")
if diploma == "ja":
  heeft_diploma = True
else:
  heeft_rijbewijs = False  

rijbewijs = input("Bent u in bezit van een geldig vrachtwagen rijbewijs? Ja/Nee")
if rijbewijs == "ja":
 heeft_rijbewijs = True
else:
  heeft_rijbewijs = False

lengte = int(input("Wat is uw lengte in cm?"))
goede_lengte = lengte >=150
if lengte <100:
  raise NameError("sorry we laten geen dwergen toe")


gewicht = int(input("Hoeveel weegt u?"))
goede_gewicht = gewicht >= 90


certificaat = input("Heeft u de certificaat Overleven met gevaarlijk personeel? Ja/Nee")
if certificaat == "ja":
  heeft_certificaat = True
else:
  heeft_certificaat = False  



sollicitatie_punten = sollicitatie and heeft_ervaring and heeft_diploma and heeft_rijbewijs and goede_lengte and goede_gewicht and heeft_certificaat
if sollicitatie_punten:
  print("u komt in aanmerking voor een sollicitatiegesprek!")

else:
    print("Helaas komt u niet in aanmerking voor een sollicitatiegesprek")


 

















  





