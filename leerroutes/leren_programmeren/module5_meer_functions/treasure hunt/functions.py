import time
from termcolor import colored
from data import *
import math

##################### M04.D02.O2 #####################
def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:   
    return amount / 5       

def copper2gold(amount:int) -> float:   
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    return personCash['gold'] + copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + platinum2gold(personCash['platinum'])

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    journeycost = ((people * COST_FOOD_HUMAN_COPPER_PER_DAY) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY)) * JOURNEY_IN_DAYS
    return round(copper2gold(journeycost),2)


##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lst = []
    for x in range(len(list)):
        if list[x][key] == value:
            lst.append(list[x])
    return lst

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    lst = getShareWithFriends(friends)
    lst = getAdventuringPeople(lst)
    return lst
##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    if people <=2:
        return 1
    elif people <=4:
        return 2
    elif people <=8:
        return 4 
    else:
        return 4 +(people - 8)// 2
pass

def getNumberOfTentsNeeded(people:int) -> int:
    if people <= 3:
        return 1
    elif people <= 6:
        return 2
    else:
        return 3
pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    horses_gold = (silver2gold(horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS)) 
    tentcosts =  tents * COST_TENT_GOLD_PER_WEEK
    rentalcost = horses_gold + tentcosts * (round(JOURNEY_IN_DAYS / 7))
    return round((rentalcost),2)
pass

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    list = []
    for index in items:
        item = f"{index['amount']}{index['unit']} {index['name']}"
        list.append(item)
    return ', '.join(list) 
pass

def getItemsValueInGold(items:list) -> float:
    gold = 0
    for index in items:
        if index['price']['type'] == 'copper':
            gold += copper2gold(index['price']['amount'] * index['amount'])
        elif index['price']['type'] == 'silver':
            gold += silver2gold(index['price']['amount'] * index['amount'])
        elif index['price']['type'] == 'gold':
            gold += index['price']['amount'] * index['amount']
        elif index['price']['type'] == 'platinum':
            gold += platinum2gold(index['price']['amount'] * index['amount'] )  
    return gold  
pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    gold = 0
    for person in people:
        cash = person['cash']
        gold += platinum2gold(cash['platinum']) + silver2gold(cash['silver']) + copper2gold(cash['copper']) + cash['gold']
    return gold
##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    lstInvestors = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            lstInvestors.append(investor)
    return lstInvestors

def getAdventuringInvestors(investors:list) -> list:
    adventuring =  getAdventuringPeople(getInterestingInvestors (investors))
    return adventuring

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totalCosts = 0

    adventuringInvestors = getAdventuringInvestors(investors)

    for investor in adventuringInvestors:
        totalCosts += getItemsValueInGold(gear)
    investorJourneyCosts = getJourneyFoodCostsInGold(len(adventuringInvestors), len(adventuringInvestors))
    investorRentalCosts = getTotalRentalCost(len(adventuringInvestors), len(adventuringInvestors))
    
    totalCosts += investorJourneyCosts + investorRentalCosts
    return totalCosts
##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    nightsininn = math.floor(leftoverGold / (people * silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) + horses * copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)))
    return nightsininn

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    journeycost = nightsInInn * (people * silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) + horses * copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT))
    print(journeycost)
    return round(journeycost,2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    lst = []
    for investor in getInterestingInvestors(investors):
        lst.append(round(investor['profitReturn'] / 100 * profitGold, 2))
    return lst

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    goud = round((profitGold - sum(investorsCuts)) / fellowship, 2) 
    print(goud)
    return goud

##################### M04.D02.O13 #####################

def get_earnings(profit_gold, main_character, friends, investors):
    people = [main_character] + friends + investors
    earnings = []

    adventuring_friends = getAdventuringFriends(friends)
    interesting_investors = getInterestingInvestors(investors)
    adventuring_investors = getAdventuringInvestors(investors)
    investors_cuts = getInvestorsCuts(profit_gold, investors)
    gold_cut = profit_gold - sum(investors_cuts)
    end_gold = 0

    for person in people:
        person['name']
        start_gold = getCashInGoldFromPeople([person])

        if person in interesting_investors and person in adventuring_investors:
            end_gold = start_gold + investors_cuts[investors.index(person)] + gold_cut / len([main_character] + adventuring_friends + adventuring_investors)
        elif person in interesting_investors:
            end_gold = start_gold + investors_cuts[investors.index(person)]
        elif person in investors and person not in interesting_investors:
            end_gold = start_gold
        elif person in adventuring_friends:
            end_gold = start_gold + (gold_cut / len([main_character] + adventuring_friends + adventuring_investors))-10
            earnings[0]['end']+=10
            print(earnings)
        elif person in friends and person not in adventuring_friends:
            end_gold = start_gold
        else:
            end_gold += start_gold + gold_cut / len([main_character] + adventuring_friends + adventuring_investors)

        earnings.append({
            'name': person['name'],
            'start': start_gold,
            'end': round(end_gold, 2)
        })

    return earnings
##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()
