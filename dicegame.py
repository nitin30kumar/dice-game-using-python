#This is a rolling dice game

import random
import time

#defining variables
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices .....")
    time.sleep(2)
    print("The values are ...")
    n1 = random.randint(min,max)
    print(n1)
    if n1 == 6:
        time.sleep(1)
        n2 = random.randint(min,max)
        print(n2)

    roll_again = input("Roll the dice again ?")

print("Thanks for playing this wonderful game..")
    
