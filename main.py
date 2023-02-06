import random

goal =0
guess = None
tries =0
score =0
keepPlaying = True


print("Let's play the guessing game. I choose a number between 1-10 and you guess.")

while(keepPlaying):
    
    # Chooses number and asks user to guess the number until chosen number is picked
    # Will output if guess is higher or lower than chosen number

    goal = int(random.random() * 10 + 1)
    guess = input("\nNew number generated, guess the number: ")

    while(True):

        tries+=1

        try:
            guess = int(guess)
        except ValueError:
            print("wtf, that's not a number?!?!")
            guess = -1

        if(guess == -1):
            guess = input("Guess the number and actually input a number: ")
        elif(guess == goal):
            score+=1
            print(f"\nYou guess the number correctly! You got the number {goal} in {tries} tries. Total Score: {score}")
            tries =0
            break
        else:
            if(guess > goal):
                print("The number is lower")
            else:
                print("The number is higher")
            guess = input("\nGuess the number: ")
        
    

    # input validation for next round, checks if player put in corect input and wants to play another 

    while(True):
        playAgain = input("\nDo you want to play again? (y/n): ")
        if(playAgain == "n" or playAgain == "N"):
            keepPlaying = False
            break
        elif(playAgain == "y" or playAgain == "Y"):
            print("New Round!")
            break
        else:
            print("Invalid input, try again: ")

print("Thanks for playing!\nFinal Score: %d\n"%(score))