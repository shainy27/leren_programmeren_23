
# verandering = 0
# i = 50
# som = i + verandering

# while i <= 2200:
# if i >= 1100:
#     break
# print(i)
# verandering = verandering + 1
# i = som + i + verandering
# print("einde")



som = 50
getal = 50
uitwerking = "50"
teller = 0

while som < 1000:
    teller += 1
    getal += 1
    som += getal
    uitwerking += " + " + str(getal)
    print(f"{teller}. {uitwerking}  =  {som}")
