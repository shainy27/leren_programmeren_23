from random import randint

leeuw = '''\       
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
            '''



huis = '''\
                                       ____
                   ____________________|  |_____
                  /______________________________\ 
                 /________________________________\  
                   ||___|___||||||||||||___|__|||     
                   ||___|___||||||||||||___|__|||        
                   ||||||||||||||||||||||||||||||

      '''


slang = '''   
                     ---_ ......._-_--.
                    (|\ /      / /| \  \\
                    /  /     .'  -=-'   `.
                  /  /    .'             )
                _/  /   .'        _.)   /
                / o   o        _.-' /  .'
                \          _.-'    / .'*|
                \______.-'//    .'.' \*|
                  \|  \ | //   .'.' _ |*|
                  `   \|//  .'.'_ _ _|*|
                    .  .// .'.' | _ _ \*|
                    \`-|\_/ /    \ _ _ \*\\
                    `/'\__/      \ _ _ \*\\
                    /^|            \ _ _ \*
                  '  `             \ _ _ \      
                                    \_
           '''
import sys, time
def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


def treasure():
    sprint("You continue on your way to the treasure and walk into a dark cave. There's a text on the wall:")
    tries = 3
    while tries > 0:
        riddle = input("Solve the riddle to win the game: Before Mount Everest was discovered, what was the highest mountain in the world?")
        if riddle.lower() == "mount everest":
            print(f"Congratulations, you found the treasure and won the game!")
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
                        "=._o--._   ;o|o;     _._;o
                             "=._o._; | ;_.--"o.--"
                                  "=.o|o_.--""
            ''')
            exit()
        else:
            tries -= 1
            if tries == 0:
                print("Game over.")
                exit()
            else:
                print(f"Incorrect answer. You have {tries} tries left. Try again.")

            