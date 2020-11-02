# *Hang Man Game*
# Author : Obaid Nadeem
# Oct 18, 2020
# Python 3.8

# Libraries used:
# Meaning and Synonyms using pypi library: Dictionary
# Link to Dictionary:  https://pypi.org/project/Py-Dictionary/

import random
from random_word import RandomWords
from pydictionary import Dictionary

def main():

    random_words = ["NewYork","Baku","Istanbul","Karachi","Jeruselam"]
    word = str(random.choice(random_words))

    # hints
    print("The word is a country name! \nThe lenght of the word is {} letters".format(len(word)))
    print("\nUse Lower case!\n ")

    correct_answer = []
    for i in range(len(word)):
        correct_answer.append("_")
    print(correct_answer)

    guess = 0

    letters_guessed = []

    while guess < len(word):
        user_guess = input("Enter a guess: ")
        if len(user_guess) != 1:
            print("Please Enter a single letter! : ")
        elif user_guess in word.lower():
            for index, letter in enumerate(word.lower()):
                if letter == user_guess:
                    correct_answer[index] = user_guess
                    print(correct_answer)
                    letters_guessed.append(user_guess)
                    # print(letters_guessed)
        else:
            user_guess not in word
            if user_guess not in letters_guessed:
                print("The letter does not exits in the word! ")
                guess += 1
                print("Your {} tries are left! ".format(len(word) - guess))
                letters_guessed.append(user_guess)
            else: 
                user_guess in letters_guessed
                print("You have alredy guessed this word! ")

        if ''.join(correct_answer) == word.lower() and guess < len(word):
            print("You Win! ")
            break   
        
        

main()


# Messed up code :(