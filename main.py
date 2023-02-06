import random

goal =0
guess = None
tries =0
score =0
keepPlaying = True


input("Let's play the guessing game. I choose a number between 1-10 and you guess.")

while(keepPlaying):
    
    # Chooses number and asks user to guess the number until chosen number is picked
    # Will output if guess is higher or lower than chosen number

    goal = random.random() * 10 + 1
    guess = input("New number generated, guess the number: ")

    if(guess == goal):
        tries+=1
        score+=1
        print("You guess the number correctly! You got the number %d, in %d. Total Score: %d", (goal, tries, score))
    else:
        if():
            print("The number is higher")
        else:
            print("The number is lower")
    

    # input validation for next round, checks if player put in corect input and wants to play another 

    while(True):
        playAgain = input("Do you want to play again? (y/n): ")
        if(playAgain == "n" or playAgain == "N"):
            keepPlaying = False
            break
        elif(playAgain == "y" or playAgain == "Y"):
            print("New Round!")
            break
        else:
            print("Invalid input, try again: ")

print("Pass")