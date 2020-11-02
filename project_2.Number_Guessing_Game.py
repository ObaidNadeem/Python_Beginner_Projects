# Number guessing game
# Author: Obaid Nadeem
# Python 3.8

import random

def noGuess():

    random_number = random.randint(0,10)
    user_guess = int(input("What is your guess ? :"))


    while True:
            
        if user_guess == random_number:
                print("You guess the number right!")
                break
                
        

        elif user_guess == random_number + 3 or user_guess == random_number - 3:

            random_number = random.randint(0,10)
            user_guess = int(input("Let's try again, What is your guess ? :"))
            print("You were close! The number was: {}".format(random_number))
        

        else:
            user_guess > random_number + 3 or user_guess < random_number - 3
            random_number = random.randint(0,10)
            user_guess = int(input("Let's try again, What is your guess ? :"))
            print("Your are wrong you nerd! The number was: {}".format(random_number))


# calling function
noGuess()
        
