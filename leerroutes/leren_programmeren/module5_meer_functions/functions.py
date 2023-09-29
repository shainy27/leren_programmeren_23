def copper2silver(copper, toSilver=True):
    if toSilver:
        return copper / 10
    else:
        return copper * 10

def silver2gold(silver, toGold=True):
    if toGold:
        return silver / 5
    else:
        return silver * 5

def copper2gold(copper, toGold=True):
    if toGold:
        return silver2gold(copper2silver(copper))
    else:
        return silver2gold(copper2silver(copper, toSilver=False), toGold=False)

def platinum2gold(platinum, toGold=True):
    if toGold:
        return platinum * 25
    else:
        return platinum / 25

def getpersonacashingold(persona_currency):
    total_gold = 0
    for currency_type, value in persona_currency.items():
        if currency_type == 'gold':
            total_gold += value
        elif currency_type == 'silver':
            total_gold += silver2gold(value)
        elif currency_type == 'copper':
            total_gold += copper2gold(value)
        elif currency_type == 'platinum':
            total_gold += platinum2gold(value)
    return total_gold

def getItemAsText(items:list) -> str:
    for item in items:
        print(item)




