name1 = input("Player 1 enter your name? ")
print(f"Welcome, {name1} to our mountainclimbing game.")
print("Your purpose is to find your way through different challenges and make your way to the top")
print()
loop = True

while loop == True:
    
    start = input("Enter PlAY to start or else die ")
    if start.lower() != "play":
        loop = False
        print("quit")
        quit()
        
    
    elif start.lower() == "play" or "Play" and start.isalpha():
        print("lets go")

    "Location 1"
    
    #Zeggen dat. de spelers een rugzak hebben en een zaklamp.    
    print(f"Player {name1} receive a ITEM [backpack] and ITEM [flashlight] to Play the game")
    print()
    
    #keuze gids volgen of zelf op pad gaan
     
    while loop == True: 
          
        if start == "play" or "Play":
            setting = input("Do you want to FOLLOW the guide or go ALONE? ")
            print()
            
        #krijg eerst een Rekensom    (1elocatie)
        if setting == "FOLLOW" or setting == "follow":
            print("To follow the guide to the next location you first must solve this puzzle")
            puzzle_1 = input("2x2= ")
            if puzzle_1 != "4":
                print("You lose, TRY AGAIN!")
                start = "play"
                continue
            else:
                print("Correct continue to next location")
                print()

        elif setting == "ALONE" or setting == "alone": 
            user = input("Do you want to turn LEFT or RIGHT? ")
            if user == "LEFT" or "RIGHT":
                print("You died, TRY AGAIN!")
            start = "play"
            continue
        else:
            print("invalid input")
            loop = False
        
        # 2e
        
        grot = input("You hear a sound coming from the cave. Do you FOLLOW the sound or AVOID it? ")
        if grot == "FOLLOW" or grot == "follow":
            print(f"{name1} grabs their flashlight out of their backpack, to find the way through the darkness.")
            print(f"Eventually {name1} reaches the sound and finds out it is coming from the ducks at the lake.")
                
        elif grot == "AVOID" or grot == "avoid":
            while loop == True:
                print(f"{name1}comes across a campers that give you the tip to take the pot of ITEM [honey] incase you come across a bear")
                print(f"All of a sudden you do come across a bear")
                bear = input(f"Do you throw the HONEY at the bear or do you RUN away screaming? ")
                if bear == "HONEY" or bear == "honey":
                    print("You distracted the bear and reaches the sound and finds out it is coming from the ducks at the lake.")
                    print()
                    break
                        
                else:
                    print("The bear is faster, TRY AGAIN")
                    grot = "AVOID"
                    continue
        
        
                

        # 4e Moet dit deel niet nog een tab terug? 
        print(f"{name1} has arrived at the lake.")
        print(f"To continue to the next location you first must play a game of hangman")
        
        word = ["h","o","i"]
        streepje = ["-","-","-"]
        allowed_errors = 5
        guesses = []
        while allowed_errors <= 5:
            done = False    
                    
            guess = input("next guess: ")
            guesses.append(guess.lower())            
            
            for letter in range(3):
                if word[letter] == guess:
                    streepje[letter] = guess
            guessedWord = "".join(str(c) for c in streepje)
            print(guessedWord)
            done = True   
            
            if guess.lower() not in word:
                allowed_errors -= 1
                if allowed_errors == 0:
                    print("You did not win any food :<")
                    break
            else:
                
                is_correct = False
                for letter in streepje:
                    if letter in word:
                        is_correct = True
                    else:
                        is_correct = False
                if is_correct and "-" not in streepje:
                    done = True
                    break
                            
        if done == True:
            print(f"You found the word, it was {guessedWord} continue to the next location")
        

            #5
            afgrond = (f" {name1} has arrived at a abyss")
            print(f"In order to survive this route {name1} must throw with the dice ")
            print("otherwise you will be crushed by a larg rock!")
            
            is_correct = False
            while is_correct == False: 
                dice = input("Give a number between 1-6 to roll the dice: ")
                if dice == "4":
                    print("Well done! you have won food [apple], [muslibar], [water]")
                    print()
                    is_correct = True
                else:
                    print("TRY AGAIN")
                    print()


            #6 
            words = ["backpack","flashlight","carabiner","hooks","food","hiking shoes"]
            drijfzand = print(f"{name1} has fallen into quicksand!")
            if done == True:
                print(f"{name1} luckily had enough food to give them energy to get out of the sand.")
                print()
               
            else:
                print("Sorry, but you do not have any food left.. For that you need to solve this next puzzle")
                puzzle = input("What is it that you need for mountainclimbing? (One anwsers is suffecient.)")
                if words in puzzle:
                    print(f"{name1} solved the puzzle and is now able to get out of the sand.")
                    loop == False
                else:
                    print("Sorry, but you lost. TRY AGAIN")
                    print()
                    grot = "AVOID"
                    grot = "avoid"
                    continue         

            #7 while loop vragen aan iemand
            kamp = print("Welcome to this camp! First solve this puzzle to get climbing equipment. ITEM [rope],[poles],[shoes],[helmet]")
            puzzle = input("")


            #8
            yeti = input("Wow u found yeti's, do you want to BEFRIEND or FIGHT them? ")
            if yeti == "BEFRIEND" or yeti == "befriend":
                print("lovely picnic")
                print()
                skipLocation = True
            elif yeti == "FIGHT" or yeti == "fight":
                print("You lost! They got all your food.")
                print("Quickly climb up to the next location!")


            #9


            #10
            if skipLocation == True:
                end = print("WELL DONE! You reached the top of the mountain :D")
                print()
                print(f"{name1} is enjoying a lovely picnic with the yeti family.")