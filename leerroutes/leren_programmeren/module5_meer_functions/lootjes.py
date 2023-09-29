import random

participants = []

loop = True
while loop:
    name = input('enter a name from one of the participants ')
    if name in participants:
        print('name already entered')
    else:
        participants.append(name)
        if len(participants) >2:
            another_name = input('do you want to enter another participant? ').lower()
            if another_name in ('nee','n','no'):
                loop = False

partners = []
random.shuffle(participants)
len_participants = len(participants)
for name in participants:
    index = (participants.index(name) +1 )% len_participants
    partners.append(participants[index])


for i in range(len(partners)):
    print(participants[i], "is partnered with", partners[i])