from fruitmand import fruitmand
# for fruit in fruitmand[1:2]:
#     print(fruit["name"],fruit["weight"])

for fruit in fruitmand:
    if fruit["name"] == "appel":
        print(fruit["name"], fruit["weight"])
