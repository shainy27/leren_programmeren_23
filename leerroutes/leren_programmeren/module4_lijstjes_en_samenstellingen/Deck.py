import random

Kaarten = ("2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas")
Kleur = ("harten ","klaveren ","schoppen ","ruiten ")
Deck = []
teller = 0

for x in Kleur:             #??
    for i in Kaarten:
        Deck.append (x[0:] + i[0:])   #de kleur + de kaartnummer in de deck zetten

Deck.append ("Joker1")  #jokers in de deck
Deck.append ("Joker2")

for y in range(7):
    RandomKaart= random.choices(Deck)
    teller += 1                        #kaarten teller
    print(f"Kaarten {teller} : {RandomKaart}")

random.shuffle(Deck)
print(Deck)