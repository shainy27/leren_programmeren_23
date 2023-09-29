#Julina Mercera
sides = int(input("Enter a number: "))

name = "" 

if (sides == 3):
    name = "triangle"

elif (sides == 4):
    name = "quadrilateral"

elif (sides == 5):
    name = "pentagon"

elif (sides == 6):
    name = "hexagon"

elif (sides == 7):
    name = "heptagon"

elif (sides == 8):
    name = "octagon"

elif (sides == 9):
    name = "nonagon"

elif (sides == 10):
    name = "decagon"

if (sides < 3):
    print(f"does not match any listed shapes")

if (sides >10):
    print(f"does not match any listed shapes")
else :
    print(f"It is a: {name}")