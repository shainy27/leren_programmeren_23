
a = int(input("voer een getal in:"))
b = int(input("voer een getal in:"))



if a > b:
    max = a
    min = b
    print(f'a is het grootste getal: {max}')

elif b > a:
    max = b
    min = a
    print(f'a is het kleinste getal: {min}')

elif a == b:
    max = a
    min = b
    print("a en b zijn even groot")

print(f"het minimum is {min}")
print(f"het maximum is {max}")



