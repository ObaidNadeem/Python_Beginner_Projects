# Python Revision part 3
# * TEXT BASED ADVENTURE GAME *
# Author: Obaid Nadeem
# Game: Escape
# Inspired from 1970's classic Text based game 'Zork', this is a nerd version of that game ...
# Python 3.8

import random

def main():
    player_name = input("Enter you name ")

    def guard():
        actions = {"sleeping" : "You escaped succesfully, the guard was sleeping",
                "caught" : "You got caught!",
                "chase" : "The guard is chasing you !"
        }
        
        guardAction = random.choice(list(actions.keys()))
        if guardAction == "sleeping":
            print("WOOHOO! You escaped successfully")
        elif guardAction == "caught":
            print("SH!T, You got caught!")
        elif guardAction == "chase":
            decision = input("Guard is chasing you, hop left or right ? ")
            if decision == "left":
                print("You escaped successfully through open door!")
                exit()
            elif decision == "right":
                print("You got caught by another guard")
       
    def choose():
        text = input("red or blue door ? ")
        if text == 'red':
            red_door()
        elif text == 'blue':
            blue_door()


    def red_door():
        print('You got eaten by a dragon \n Game Over !')
        exit()

    def blue_door():
        print('There is a guard outside, You have to escape him {}, \n Do you want to escape him ? y / n '.format(player_name))    
        decision = input('>')
        if decision == 'y':
            guard()
        elif decision == 'n':
            print('red or blue door ? ')
            pass
        



    while True:
        choose()
        

main()



