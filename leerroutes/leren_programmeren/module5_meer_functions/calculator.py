# functies voor optellen,aftrekken,vermenigvuldigen en delen
def optellen(num1, num2):
    return num1 + num2

def aftrekken(num1, num2):
    return num1 - num2

def vermenigvuldigen(num1, num2):
    return num1 * num2

def delen(num1, num2):
    return num1 / num2

# num1 
num1 = None
choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
extra = True

# functie om de tweede getal te krijgen van de user
def get_num(vraag):
    while True:
        try:
            return float(input(vraag))
        except:
            print("Voer een geldig getal in")


# functie om de keuze te krijgen
def get_choice():
    return input('\nWat wil je doen? \n A) optellen \n B) aftrekken \n C) vermenigvuldigen \n D) delen \n E) verhogen \n F) verlagen \n G) verdubbelen \n H) halveren \n I) stop \n Kies een letter: ').lower()

# main loop
while extra:
    # als num1 nog niet is gegeven vraagt het voor num1
    if num1 is None:
        num1 = get_num('What is the number? ')

    # Vraagt voor de keuze
    choice = get_choice()

    # Doe de operatie en print het resultaat
    if choice in choices:
        if choice == 'a':
            num2 = get_num("Voer getal in")
            result = optellen(num1, num2)
            print(f'Het antwoord is {result}')
        elif choice == 'b':
            num2 = get_num("Voer getal in")
            result = aftrekken(num1, num2)
            print(f'Het antwoord is {result}')
        elif choice == 'c':
            num2 = get_num("Voer getal in")
            result = vermenigvuldigen(num1, num2)
            print(f'Het antwoord is {result}')
        elif choice == 'd':
            num2 = get_num("Voer getal in")
            result = delen(num1, num2)
            print(f'Het antwoord is {result}')
        elif choice == 'e':
            result = optellen(num1, 1)
            print(f'Het antwoord is {result}')
        elif choice == 'f':
            result = aftrekken(num1, 1)
            print(f'Het antwoord is {result}')
        elif choice == 'g':
            result = vermenigvuldigen(num1, 2)
            print(f'Het antwoord is {result}')
        elif choice == 'h':
            result = delen(num1, 2)
            print(f'Het antwoord is {result}')

        # vraagt of de user het resultaat als num1 wil gebruiken in de volgende calculatie
        choice2 = input(f'\n wil je het resultaat: {result} gebruiken als het eerste getal? (j/n)  \n Of stop programma (stop)  ').lower()
        if choice2 == 'j':
            num1 = result
        elif choice2 == 'stop':
            extra = False
            print('dag!')
        else:
            num1 = None

    # als de user i kiest stopt het programma
    elif choice == 'i':
        extra = False
        print('Dag!')
        
    # als je niet een geldig letter invoert:
    else:
        print('Kies een geldig letter')