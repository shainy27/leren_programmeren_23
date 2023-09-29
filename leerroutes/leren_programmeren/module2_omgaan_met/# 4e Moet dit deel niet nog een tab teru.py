# 4e Moet dit deel niet nog een tab terug? 
        print(f"{name1} has arrived at the lake.")
        print(f"To continue to the next location you first must play a game of hangman")
        
        word = ["h","o","i"]
        streepje = ["-","-","-"]
        allowed_errors = 5
        guesses = []
        while allowed_errors => 5:
            done = True    
                    
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
                    print("Well done! you have won food ITEM [apple], [muslibar], [water]")
                    print()
                    is_correct = True
                else:
                    print("TRY AGAIN")
                    print()


            #6 
            words = ["backpack","flashlight","carabiner","hooks","food","hiking shoes"]
            drijfzand = print(f"{name1} has fallen into quicksand!")
            if is_correct == True:
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