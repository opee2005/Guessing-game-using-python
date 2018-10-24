print('''This program is written by lawal opeyemi
      Email address: opee2005ng@yahoo.com
      Phone number: 08087655247''')
import datetime
from random import *
today = datetime.datetime.now()
Date = "{today.day}/{today.month}/{today.year}".format(today=today)
print(Date)
player_1 = input("player_1's name: ")
player_2 = input("player_2's name: ")
player_3 = input("player_3's name: ")
players = [player_1, player_2, player_3]
shuffle(players)
for p in players:
    print(p,"it's your turn ")
    secret_number = randint(1,39) #random number between 1 and 39
    for number_guesses in range(5): #you are to provide 5 numbers, one at a time 
         guess_number = eval(input("pleese enter your guess number beteween 1 and 39 (1-39): "))
         if guess_number < secret_number:
             print("HIGHER.", (5-number_guesses)-1, ":guesses left.\n")
         elif guess_number > secret_number:
             print("LOWER.", (5-number_guesses)-1, ":guesses left.\n")
         else:
             print("WAHOOOOOO!!!!!!!!! YOU GOT IT, CONGRATULATION TO YOU",p)
             break
    else:
       print(" oh no! you lose. The correct number is ", secret_number, ".Hope you enjoy it, come back later for another trial")
        
                        
