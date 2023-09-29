
boodschappenlijst = {} 
doorgaan = True
while doorgaan: 
    item = input("Voeg een item toe aan uw boodschappenlijst  ").capitalize()
    aantal = int(input("Hoeveel van deze item wilt u hebben?"))
    
    if item in boodschappenlijst:
            boodschappenlijst[item]+=aantal
    else:
            boodschappenlijst[item]=aantal

    while True:
        door = input("Wilt u nog een item toevoegen?  ").lower()   #nog een item toevoegen?
        if door in ("nee"):
            doorgaan = False
            break
        if door in ("ja"):
            break
            
print("")
print("-[Boodschappenlijst]-")   #print boodschappenlijst
print("")
print(boodschappenlijst)
print("______________________")






