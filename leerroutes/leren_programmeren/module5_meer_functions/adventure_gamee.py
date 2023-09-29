from threading import Event
from random import randint
import sys, time
from adventure_game_art import *



from random import randint

def game_over():
    play_again = input("Do you want to play again? Y/N")
    if play_again in ["Y", "y", "yes", "Yes"]:
        return
    elif play_again in ["N", "n", "no", "No"]:
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid input, please enter Y or N.")


def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)



def points(health, energy, score):
    print(f'''Your health, energy, and score are now:
      health: {health}
      energy: {energy}
      score: {score}   
      ''')
    
    if health <= 0 or energy <= 0:
        print("You don't have enough points to continue. Game over!")
        play_again = input("Do you want to play again? Y/N")
        if play_again in ("Y", "y", "yes", "Yes"):
            play_game()
        else:
            return False

    elif score >= 5:
        print("Congratulations, you found the treasure and won the game!")
        play_again = input("Do you want to play again? Y/N")
        if play_again in ("Y", "y", "yes", "Yes"):
            play_game()
        else:
            return False

    return score

def make_skill_check(skill_name):
    # skill check met 50% kans om te lukken
    result = randint(1, 2)

    if result == 1:
        print(f"You succeeded in your {skill_name} check!")
        return True
    
    else:
        print(f"You failed your {skill_name} check!")
        return False
    

def swim_river(health, energy, score):
    print("You come across a river. You can either try to swim across or build a raft.")
    choice = input("Do you want to swim or build a raft? swim/build  ").lower()

    if choice in ["swim", "s"]:
        if make_skill_check("swimming"):
            sprint("You successfully swam across the river!")
            score += 1
            points(health, energy, score)

        else:
            sprint("The current is too strong and you get swept away. You lose 2 health points !")
            health -= 2
            points(health, energy, score)

    elif choice in ["build", "b"]:
        if make_skill_check("survival"):
            sprint("You successfully build a makeshift raft and cross the river!")
            score += 1
            points(health, energy, score)
            Event().wait(1)

        else:
            sprint("You're unable to build a raft and lose 2 energy points.")
            energy -= 2
            points(health, energy, score)

    elif choice in ["look", "l"]:
        sprint("You spend some time looking for a bridge and eventually find one!")
        score += 1
        points(health, energy, score)
        
    else:
        sprint("Invalid input. Please choose to swim, build a raft, or look for a bridge.")
        swim_river(health, energy, score)




def play_game():

    health = 3
    energy = 3
    max_health = 3
    max_energy = 3
    score = 0


    name = input("What is your name?")

    # uitleg voor de game
    sprint(f"Welcome to the jungle {name}! In this game you will make your way through the")
    sprint("dangerous jungle in an attempt to find the hidden treasure. ")
    sprint("You also need to make sure your health and energy bar dont run out!")
    sprint("If you make the right choices along the way you will score points. If you make all the right choices you automatically win the game!")


    Event().wait(3)

    #Slang

    while True:
        print(slang)
        snake = input("As you start exploring the jungle you hear noises coming from behind you. It's a snake! Fight the snake or Run? Run/Fight:").lower()
        if snake in ("fight", "f"):
            print("You try to fight the snake with your bare hands and get bitten. You lose 1 health point!")
            health -= 1
            break

        elif snake in ("run", "r"):
            sprint("You run away and escape the snake! The running made you tired. You lose 1 energy point!")
            energy -= 1
            score += 1
            break

        else:
            print("Please enter a valid choice!")

    Event().wait(1)
    points(health, energy, score)
    Event().wait(1)

    swim_river(health,energy,score)

    while True:
        answer = input("You're walking through The jungle when suddenly you find a small lake with muddy water. Take a sip of water? Y/N:").lower()

        if answer in ("y","yes"):
            sprint("You take a sip of the muddy water. Why would you do that? You lose a health point!")
            health -=1
            break

        if answer in ("n", "no"):
            print("You continue walking.")
            score += 1
            break

        else:
            print("please enter a valid choice!")

    Event().wait(1)
    points(health, energy, score)
    Event().wait(1)


    while True:
        print(huis) 
        huisje = input("You continue on your path to find the treasure. You see an abandoned wooden house. Do you want to explore it? Y/N")

        if huisje in ("y" ,"yes",):
            print("You enter the house. There haven't been any people here for a while. You find a tiny mattress. It seems comfortable enough.")
            score += 1
            rest = input("You can stay the night to restore all your health and energy points. Stay the night?")

            if rest in ("yes", "y"):
                health = max_health
                energy = max_energy
                print("You stay the night, your energy and health points are back to", max_health, "!")
                print("You get up the next morning and continue on your journey")
                score += 1
                break
            
            if rest in ("n", "no"):
                print("You decide not to stay the night and continue on your journey") 
                print("When you get back outside you realize a spider has bitten you! You lose 2 health points!")
                health -= 2
                break
        
        if huisje in ("n","no"):
            print("You decide not to enter the house. You come across a strange statue that tells you to test your might.")
            might = input("Do you wish to test your might? If you lose the test you go game over! Y/N:  ")
            if might in ("yes","y"):
                success = randint(0,1) # randomly generates a 0 or 1
                if success == 1:
                    sprint("You successfully test your might! The statue dispenses the piece of the map you were missing.")
                    sprint("Now you can succesfully find the treasure")
                    treasure()
                else:
                    print("You fail the test of might... Game Over!")
                    game_over()
            else:
                print("You decide not to test your might.")
                break
                
        
    Event().wait(1)
    points(health, energy, score)
    Event().wait(1)


    while True:

        print(leeuw)  
        lion = str(input("You continue on your path when you come face to face with a lion. fight or run? Fight/Run")).lower()
        if lion in ("fight","f"):
            sprint("The tiger charges towards you. You grab a rock on the floor and hurt him. You manage to escape and continue on your way.")
            sprint("You lose an energy point!")
            energy -=1
            score += 1
            break
        
        if lion in ("run","r"):
            print("You try to run away. The lion is too fast and catches up with you. You get eaten alive. Game Over")
            game_over()

    Event().wait(1)
    points(health, energy, score)
    Event().wait(1)


    fruit = str(input("you see some bananas hanging on a tree. Do you want to climb the tree and grab the bananas? Y/N")).lower()
    if fruit in ("y", "yes"):
        sprint("You climb the tree to grab the fruit when you see a group of monkeys in front of you. They fight you for the bananas. You end up falling to your death. Game Over!")
        game_over()

    if fruit in ("n","no"):
        sprint("You continue walking")
        score += 1

    Event().wait(1)
    points(health, energy, score)
    Event().wait(1)


    while True:      
            help = input("You keep walking and see an old tired man sitting on a tree trunk. Talk to him? Y/N").lower()
            if help in ("yes","y"):
                sprint("\'Hello there, I bet you're also looking for the treasure arent ya.\'")
                sprint("\'It's right over there in the cave. But to get to it you need to solve a riddle. I couldn't solve it, you should try your luck\'")
                Event().wait(1)
                treasure()


            if help in ("no","n"):
                swim = input("You walk past the stranger. You then find a small body of water. Take a swim? Y/N").lower()
                if swim in ("yes", "y"):
                    sprint("You get into the body of water to relax. Then you start to feel movement in the water. There's piranhas in the water!")
                    sprint("You try to get out but it's too late, you get attacked. Game over!")
                    game_over()

                if swim in ("no","n"):
                    sprint("You decide not to take a swim and continue walking.")
                    treasure()


                else:
                    print("Please enter a valid response!")
                    
            else:
                print("Please enter a valid response!")

play_game()






