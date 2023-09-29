import random

# lege list
deelnemers = []
invoeren=True

while invoeren:
    # Vraagt voor de naam van de deelnemers
    naam = input("Vul de naam van de deelnemer in:  ")
    # Is de naam uniek?
    if naam not in deelnemers:
        # Voegt naam toe aan de list
        deelnemers.append(naam)
        # Vraagt of je meer namen wil invoeren
        if len(deelnemers) >=3:
            doorgaan = input("Wil je nog een naam invoeren?").lower()
            if doorgaan in ("nee", "n"):
                invoeren=False
    else:
        print("Naam is al ingevoerd, Vul een andere naam in aub.")

#Lege dictionary 
partners = {}


lootjes_verdelen = True
while lootjes_verdelen:
    #Sample kiest random namen uit de lijst, len(deelnemers) is voor de hoeveelheid namen
    shuffled_namen = random.sample(deelnemers, len(deelnemers)) 
    lootjes_verdelen = False
    #Als een naam gelijk is aan de ander shuffled het opnieuw
    for i in range(len(deelnemers)):  
        if shuffled_namen[i] == deelnemers[i]: 
            lootjes_verdelen = True

#koppelt de namen in de dictionary 
for naam in range(len(deelnemers)):             
    partners.update({deelnemers[naam] : shuffled_namen[naam]})

# Print de dictionary
for naam, partner in partners.items(): 
    print(f"{naam} heeft {partner}.")