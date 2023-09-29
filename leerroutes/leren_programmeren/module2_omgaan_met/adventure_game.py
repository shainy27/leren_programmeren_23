#Adventure game

from queue import Empty
from adventure_game_art import slang




def main():

    
    
    
    
    
    from threading import Event
    import sys,time
    def sprint(str):
     for c in str + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(3./90)

    health = 3
    energy = 3






    #hier word je naam gevraagd
    name = input("What is your name?")


    #uitleg voor de game
    sprint(f"Welcome to the jungle {name}! In this game you will make your way through the")
    sprint("dangerous jungle in an attempt to find the hidden treasure. ") 
    sprint("You also need to make sure your health and energy points dont run out! You start with 3 points.")
          



    #hier word er gevraagd of de user wil spelen
    while True:
        play = str(input("Are you ready to play? Y/N"))

        if play in ( "N" ,"n", "no" , "No") :
          print('''Till next time!
          ''')
          exit()
        
        elif play in ("Y", "y" ,"yes","Yes"):
          sprint("Good luck on your adventure!")
          break

        else:
            print('''Please enter a valid choice
            ''')
            continue
  

    
    Event().wait(1)  
    #je komt een slang tegen, je krijgt de keuze om te vechten of te rennen
    while True:  
      print(slang)

      snake = input("As you start exploring the jungle you hear noises coming from behind you. It's a snake! Fight the snake or Run? Run/Fight:")
      if snake in ("run", "r", "Run", "RUN") +  ("Fight", "f", "fight", "FIGHT"):
        break
      else:
         print("Please enter a valid choice!")
        
    if snake in ("run", "r", "Run", "RUN"):
      energy = energy - 1
      sprint("You run away and escape the snake! The running made you tired. You lose an energy point!")
      print(f'''Your health and energy points are now:
      health: {health}
      Energy: {energy}     
      ''')
      Event().wait(2) 
    
    elif snake in ("Fight", "f", "fight", "FIGHT"):
      health = health - 2
      print("You try to fight the snake with your bare hands and get bitten. You lose 2 health points!")
      print(f'''Your health and energy points are now:
      health: {health}
      Energy: {energy}   
      ''')
      Event().wait(2)
      if (health) <= 0 or (energy) <=0 :
          sprint("You don't have enough points to continue. Game over!")
          exit()

    Event().wait(2)



    #je krijgt de keuze om water te drinken
    while True:

      answer = input("You're walking through The jungle when suddenly you find a small lake with muddy water. Take a sip of water? Y/N:")
      if answer in ("Y", "y" , "yes", "Yes"):
        health = health - 1
        sprint("You go take a sip of the muddy water. The water is full of bacteria. You lose a health point!")
        sprint(f'''Your health and energy points are now:
        health: {health}
        Energy: {energy}      
        ''')
        if (health) <= 0 or (energy) <=0 :
           sprint("You don't have enough points to continue. Game over!")
           exit()
        else:
             break

      elif answer in ("N", "n", "no", "No"):
        print("You continue walking")
        break

      else:
        print("please enter a valid choice!")
        continue

    

    #je vind een verlaten huisje met een deel van de map erin, als je naar binnen gaat kan je de game sneller winnen
    while True:
      print(r'''\
                                       ____
                   ____________________|  |_____
                  /______________________________\ 
                 /________________________________\  
                   ||___|___||||||||||||___|__|||     
                   ||___|___||||||||||||___|__|||        
                   ||||||||||||||||||||||||||||||

      ''')
      
      huisje = str(input("You continue on your path to find the treasure. You see an abandoned wooden house. Do you want to explore it? Y/N"))
      if huisje in ("Yes", "y" ,"YES", "yes", "Y"):
        health = 3
        sprint("You enter the house and find another piece of the map. Now you can get there faster!")
        sprint("You find two bars of chocolate on the counter, Your health is completely restored!")
        rest = input("You can stay the night to restore all your energy points. Stay the night?")

        if rest in ("yes", "Yes", "YES", "Y", "y"):
          health = 3
          energy = 3
          sprint("You stay the night, your energy and health points are back to 3!")
          sprint("You get up the next morning and continue on your journey")
          

        if rest in ("N", "n", "no", "No"):
          sprint("You decide not to stay the night and continue on your journey") 
          sprint(f'''Your health and energy points are now:
          health: {health}
          Energy: {energy}      
          ''')
          sprint("When you get back outside you realize a spider has bitten you! You lose a health and energy point")
          health = health - 1
          energy = energy - 1
          sprint(f'''Your health and energy points are now:
          health: {health}
          Energy: {energy}      
          ''')
          if (health) <= 0 or (energy) <=0 :
            sprint("You don't have enough points to continue. Game over!")
            exit()
          

        while True:      
         help = input("You keep walking and see an old tired man sitting on a tree trunk. Talk to him? Y/N")
         if help in ("yes", "Yes", "YES", "Y", "y"):
            sprint("\'Hello there, I bet you're also looking for the treasure arent ya.\'")
            sprint("\'It's right over there in the cave. But to get to it you need to solve a riddle. I couldn't solve it, you should try your luck\'")
            break

         if help in ("no" , "No", "NO", "n", "N"):
              swim = input("You walk past the stranger. You then find a small body of water. Take a swim? Y/N")
              if swim in ("yes", "Yes", "YES", "Y", "y"):
                sprint("You get into the body of water to relax. Then you start to feel movement in the water. There's piranhas in the water!")
                sprint("You try to get out but it's too late, you get attacked. Game over!")
                exit()

              else:
                break
         else:
            print("Please enter a valid response!")



        #je krijgt de keuze om bananen te gaan halen
        fruit = str(input("you see some bananas hanging on a tree. Do you want to climb the tree and grab the bananas? Y/N"))
        if fruit in ("Yes", "y", "YES", "yes", "Y"):
         sprint("You climb the tree to grab the fruit when you see a group of monkeys in front of you. They fight you for the bananas. You end up falling to your death. Game Over!")
         exit()

        #je krijgt een raadsel dat je op moet lossen, je krijgt 3 kansen
        if fruit in ("N", "n", "no", "No"):
          print("You continue on your way to the treasure and walk into a dark cave. There's a text on the wall:")
          print("Before Mount Everest was discovered, what was the highest mountain in the world?")
          riddle = str(input("Solve te riddle to win the game:"))
          if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
            print("Congratulations {name} you found the treasure and won the game!")
            print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
          ''')
            exit()
          
          else:
            print(f"That isn't right {name}. 2 more tries left!")
            print("Before Mount Everest was discovered, what was the highest mountain in the world?")
            riddle = str(input("Solve te riddle to win the game:"))
            if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
              print(f"Congratulations {name} you found the treasure and won the game!")
              print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
              exit()

            else:
              print(f"That isn't right {name}. 1 more try left!")


              print("Before Mount Everest was discovered, what was the highest mountain in the world?")
            riddle = str(input("Solve te riddle to win the game:"))
            if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
              print(f"Congratulations {name} you found the treasure and won the game!")
              print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
              exit()

            else:
              print(f"That isn't right {name}. No more tries left. Game Over!")
              exit()
            
      #als je het huisje beslist niet in te gaan kom je een leeuw tegen     
      if huisje in ("N", "n", "no", "No"):
        sprint("You walk past the house.")
        Event().wait(1)
        print(r'''\       
                                 .-.       .-.
                                (   \_.-._/   )
                                 \           /
                                 | __     __ |
                                 | \O\   /O/ |
                                  \  "   "  /
                                  /\_`-v-'_/\
                                 /  \._|_./  \
                                |    \___/    |
                                |             |
                                |             |
                                |   |     |   |
                      .ww.     _|   |     |   |_
                    .\WWW=    / |   |     |   | \
                    \WWW=    |  |   |     |   |  |
                    \WW=     |  |   |     |   |  |
                    ( (      |  |   \     /   |  |
                    \ \___.-'\  \   \   /   /  /
                      `-.__.-(...(...)---(...)...)
        ''')
        
        lion = str(input("You continue on your path when you come face to face with a lion. fight or run? Fight/Run"))
        if lion in ("Fight", "fight",):
          sprint("The tiger charges towards you. You grab a rock on the floor and manage to hurt him. You manage to escape and continue on your way")
          sprint("You lose an energy point!")
          energy = energy - 1
          sprint(f'''Your health and energy points are now:
                  health: {health}
                  Energy: {energy}      
                  ''')



          sprint("You find a small wooden hut under an apple tree.") 
          resting = input("Resting and eating an apple will restore a health point and an energy point. Rest here? Yes/No")

          if resting in ("Yes", "y" ,"YES", "yes", "Y"): 
            health = health + 1
            energy = energy + 1
            sprint("You decide to take a rest and eat some apples. A health and energy point got restored!")
            sprint(f'''Your health and energy points are now:
                  health: {health}
                  Energy: {energy}      
                  ''')
            if (health) <= 0 or (energy) <=0 :
              sprint("You don't have enough points to continue. Game over!")
              exit()
            

          if resting in ("No", "n" ,"NO", "no", "N"): 
            sprint("You decide not to rest and keep exploring the jungle")



          #je krijgt de keuze om bananen te halen
          fruit = str(input("You see some bananas hanging on a tree. Do you want to climb the tree and grab the bananas? Y/N"))
          if fruit in ("Yes", "y" ,"YES", "yes", "Y"):
            print("You climb the tree to grab the fruit when you see a group of monkeys in front of you. They fight you for the bananas. You end up falling to your death. Game Over!")
            exit()
            
           
          if fruit in ("N", "n", "no", "No"):
            print("You continue walking")

          help = str(input("You keep walking and see an old tired man sitting on a tree trunk. Talk to him? Y/N"))
          


          if help in ("no" , "No", "NO", "n", "N"):
            swim = input("You walk past the stranger. You then find a small body of water. Take a swim? Y/N")
            if swim in ("yes", "Yes", "YES", "Y", "y"):
              sprint("You get into the body of water to relax. Then you start to feel movement in the water. There's piranhas in the water!")
              sprint("You try to get out but it's too late, you get attacked. Game over!")
              exit()

            if swim in ("no" , "No", "NO", "n", "N"):
              sprint("You decide not to take a swim and continue walking until you reach a cave.")
              sprint("You continue on your way to the treasure and walk into a dark cave. There's a text on the wall:")
              print("Before Mount Everest was discovered, what was the highest mountain in the world?")
              riddle = str(input("Solve te riddle to win the game:"))
              if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
                print(f"Congratulations {name} you found the treasure and won the game!")
                print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
                exit()

              else:
                  print(f"That isn't right {name}. 2 more tries left!")
                  print("Before Mount Everest was discovered, what was the highest mountain in the world?")
                  riddle = str(input("Solve te riddle to win the game:"))
                  if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
                    print("Congratulations you found the treasure and won the game!")
                    print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
                    exit()

                  else:
                     print(f"That isn't right {name}. 1 more try left!")
                     print("Before Mount Everest was discovered, what was the highest mountain in the world?")
                     riddle = str(input("Solve te riddle to win the game:"))
                     if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
                      print(f"Congratulations {name} you found the treasure and won the game!")
                      print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
                      exit()

                     else:
                      print(f"That isn't right {name}. No more tries left. Game Over!")
                      exit()


          if help in ("yes", "Yes", "YES", "Y", "y"):
           sprint("\'Hello there, I bet you're also looking for the treasure aren't you.\'")
           sprint("\'It's right over there in the cave. But to get to it you need to solve a riddle. I couldn't solve it, you should try your luck\'")

          sprint("You continue on your way to the treasure and walk into a dark cave. There's a text on the wall:")
          print("Before Mount Everest was discovered, what was the highest mountain in the world?")
          riddle = str(input("Solve te riddle to win the game:"))
          if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
            print(f"Congratulations {name} you found the treasure and won the game!")
            print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
            exit()

          else:
              print(f"That isn't right {name}. 2 more tries left!")
              print("Before Mount Everest was discovered, what was the highest mountain in the world?")
              riddle = str(input("Solve te riddle to win the game:"))
              if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
                print(f"Congratulations {name} you found the treasure and won the game!")
                print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
                exit()

              else:
                 print(f"That isn't right {name}. 1 more try left!")
                 print("Before Mount Everest was discovered, what was the highest mountain in the world?")
                 riddle = str(input("Solve te riddle to win the game:"))
                 if riddle in ("mount everest", "Mount Everest", "mount Everest", "Mount everest"):
                  print(f"Congratulations {name} you found the treasure and won the game!")
                  print('''        
                           .=""_;=.
                       ,-"_,=""     `"=.
                       "=._o`"-._        `"=.
                           `"=._o`"=._      _`"=._                    
                                :=._o "=._."_.-="'"=.
                         __.--" , ; `"=._o." ,-"""-._ ".  
                      _._"  ,. .` ` `` ,  `"-._"-._   ".'
                      |o`"=._` , "` `; .". ,  "-._"-._; ;           
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      |o;._    "      `".o|o_.--"    ;o;
                       "=._o--._        ; | ;        ; ;
                            "=._o--._   ;o|o;     _._;o;
                                 "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""
    ''')
                  exit()

                 else:
                  print(f"That isn't right {name}. No more tries left. Game Over!")
                  exit()


          
        #als je met de leeuw probeert te vechten ben je game over
        if lion in ("Run", "run"):
          print("You try to run away. The lion is too fast and catches up with you. Game Over")
          exit()

      
        else:
            print("Please enter a valid answer")






     
        



    






      
        

    




    


  

    

   

    




    

  













main()