# Python Revision
# * Python Dice Rolling Simulator *
# Author: Obaid Nadeem
# Python 3.8

import random

def main ():
    


    def dice():
        if random_number == 1:
            print ("[   ]\n[ 0 ]\n[   ]")
        elif random_number == 2:
            print ("[0  ]\n[   ]\n[  0]")
        elif random_number == 3:
            print ("[0  ]\n[ 0 ]\n[  0]")
        elif random_number == 4:
            print ("[0 0]\n[   ]\n[0 0]")
        elif random_number == 5:
            print ("[0 0]\n[ 0 ]\n[0 0]")
        elif random_number == 6:
            print ("[0 0]\n[0 0]\n[0 0]")
    
    again = True

    while again:
        random_number = random.randint(1,6)
        print(random_number)
        dice()


        again = input("Repeat? Say y or n: ")

        if again == 'n':
            exit()

main()
        
        

    
        