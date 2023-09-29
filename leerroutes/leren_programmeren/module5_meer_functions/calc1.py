# functies voor optellen,aftrekken,vermenigvuldigen en delen
def optellen(num1, num2):
    return num1 + num2

def aftrekken(num1, num2):
    return num1 - num2

def vermenigvuldigen(num1, num2):
    return num1 * num2

def delen(num1, num2):
    return num1 / num2

# Initialize num1, choices, and extra as global variables
num1 = None
choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
extra = True

# Define a function to get the second number from user
def get_num2():
    return float(input('What is number 2? '))

# functie om de keuze te krijgen
def get_choice():
    return input('\nWhat do you want to do? A) add, B) subtract, C) multiply, D) divide, E) increase, F) decrease, G) double, H) half, I) quit? \nChoose a letter: ').lower()

# loop
while extra:
    # als num1 nog niet is gegeven vraagt het voor num1
    if num1 is None:
        num1 = float(input('What is the number? '))

    # vraagt voor de keuze
    choice = get_choice()

    # Perform the chosen operation and print the result
    if choice in choices:
        if choice == 'a':
            num2 = get_num2()
            result = optellen(num1, num2)
            print(f'The answer is {result}')
        elif choice == 'b':
            num2 = get_num2()
            result = aftrekken(num1, num2)
            print(f'The answer is {result}')
        elif choice == 'c':
            num2 = get_num2()
            result = vermenigvuldigen(num1, num2)
            print(f'The answer is {result}')
        elif choice == 'd':
            num2 = get_num2()
            result = delen(num1, num2)
            print(f'The answer is {result}')
        elif choice == 'e':
            result = optellen(num1, 1)
            print(f'The answer is {result}')
        elif choice == 'f':
            result = aftrekken(num1, 1)
            print(f'The answer is {result}')
        elif choice == 'g':
            result = vermenigvuldigen(num1, 2)
            print(f'The answer is {result}')
        elif choice == 'h':
            result = delen(num1, 2)
            print(f'The answer is {result}')

        # Ask the user if they want to use the result as the first number for the next calculation
        choice2 = input(f'\nDo you want to use {result} as number 1? (Y/N) ').lower()
        if choice2 == 'y':
            num1 = result
        else:
            num1 = None

    # If the user chooses to quit, exit the loop
    elif choice == 'i':
        extra = False
        print('Goodbye!')
        
    # If the user enters an invalid choice, prompt them to choose again
    else:
        print('Invalid choice. Please choose a letter from A to I.')