import time
from termcolor import colored
from data import *

##################### M04.D02.O2 #####################

def copper2silver(amount: int) -> float:
    return amount / 10

def silver2gold(amount: int) -> float:
    return amount / 5

def copper2gold(amount: int) -> float:
    silver_amount = copper2silver(amount)
    gold_amount = silver2gold(silver_amount)
    return gold_amount

def platinum2gold(amount: int) -> float:
    return amount * 25


def getPersonCashInGold(personCash: dict) -> float:
    """
    Calculates the amount of gold a person has based on the amount of cash they have in various currencies.
    """
    total_gold = 0
    total_gold += copper2gold(personCash.get('copper', 0))
    total_gold += silver2gold(personCash.get('silver', 0))
    total_gold += personCash.get('gold', 0)
    total_gold += platinum2gold(personCash.get('platinum', 0))
    return total_gold

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    journeycost = ((people * COST_FOOD_HUMAN_COPPER_PER_DAY) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY)) * JOURNEY_IN_DAYS
    return round(copper2gold(journeycost),2)

    pass

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lst = [] 
    for x in range(len(list)):
        if list[x][key] == value:
           lst.append(list[x])
    return lst            

    pass
def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True )
    pass

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True )
    pass

def getAdventuringFriends(friends:list) -> list:
    lijst = getShareWithFriends(friends)
    lijst = getAdventuringPeople(lijst)
    return lijst
    pass

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
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

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

