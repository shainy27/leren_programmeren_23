def naam_en_leeftijd():
    # Functie die vraagt voor naam en leeftijd
    naam = input("Wat is uw naam:  ").capitalize()
    leeftijd = int(input("Wat is uw leeftijd:  "))
    # Zet de key en value in een dictionary
    return {"naam": naam, "leeftijd": leeftijd}

mensen = []

invoeren = True
while invoeren:
    persoon = naam_en_leeftijd()
    mensen.append(persoon)
    # Vraagt of je nog een naam wil invoeren
    invoeren = input("Wil je nog een naam invoeren?").lower()
    if invoeren in ("nee","n","no"):
        invoeren=False

# Gaat de lijst langs en print de dictionary
for mens in mensen:
    print(mens["naam"], "is", mens["leeftijd"],"jaar")

   



