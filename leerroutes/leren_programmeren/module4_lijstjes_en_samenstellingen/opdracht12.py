from fruitmand import fruitmand

fruitmand.sort(reverse=True, key = lambda fruit:len(fruit['name']))
print(f' De {fruitmand[0]["name"]} {len(fruitmand[0]["name"])} letters heeft een {fruitmand[0]["color"]} kleur')
