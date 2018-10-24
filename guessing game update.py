import datetime
from random import *
today = datetime.datetime.now()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)
player_names = []
number_player = int(input("number of players: "))
for i in range(0,number_player):
    name = input( "player's name: ")
    name = name.upper()
    player_names.append(name)
players = player_names    
shuffle(players)
for p in players:
    print(p,"it's your turn ")
    secret_number = randint(1,39) #random number between 1 and 39
    for number_guesses in range(5): #you are to provide 5 numbers, one at a time 
         guess_number = eval(input("pleese enter your guess number beteween 1 and 39 (1-39): "))
         if guess_number < secret_number:
             print(p,": It is HIGHER.", (5-number_guesses)-1, ":guesses left.\n")
         elif guess_number > secret_number:
             print(p,": It is LOWER.", (5-number_guesses)-1, ":guesses left.\n")
         else:
             print("WAHOOOOOO!!!!!!!!! YOU GOT IT, CONGRATULATION TO YOU",p)
             break
    else:
       print(" oh no! you lose. The correct number is ", secret_number, ".Hope you enjoy it, come back later for another trial")
        
