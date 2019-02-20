import datetime
from random import *
today = datetime.datetime.now()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)
print("WELCOME TO GUESSING GAME, ITS A FIVE(5) STAGES GAME")
print("AS YOU ADVANCE TO NEXT STAGE THE HARDER IT BECOMES")
print("GAME STARTS NOW..... ")
player_names = []
number_player = int(input("Number of Player: "))
for i in range(0,number_player):
    Name = input( "Player's Name: ")
    Name = Name.upper()
    player_names.append(Name)
Players = player_names    
shuffle(Players)
for p in Players:
    print("WELCOME, GET IT RIGHT AND MOVE TO THE NEXT LEVEL. YOU HAVE FIVE(5) ATTEMPTS, WISH YOU LUCK ")
    print(p,"It's Your Turn ")
    secret_number = randint(1,39) #random number between 1 and 39
    for number_guesses in range(5): #you are to provide 5 numbers, one at a time 
         guess_number = eval(input("Please Enter Your Guess Number Between 1 and 39 (1-39), Press Enter key to Continue: "))
         if guess_number < secret_number:
             print(p,": It is HIGHER.", (5-number_guesses)-1, "Guesses Left.\n")
         elif guess_number > secret_number:
             print(p,": It is LOWER.", (5-number_guesses)-1, "Guesses Left.\n")
         else:
             print("WAHOOOOOO!!!!!!!!! YOU GOT IT, LEVEL ONE(1) COMPLETED")
             print("WELCOME TO LEVEL TWO(2), YOU HAVE FOUR ATTEMPTS. WISH YOU LUCK ")
             secret_number = randint(1,39) #random number between 1 and 39
             for number_guesses in range(4): #you only have four attempts, one at a time 
                  guess_number = eval(input("Please Enter Your Guess Number Between 1 and 39 (1-39), Press Enter key to Continue: "))
                  if guess_number < secret_number:
                      print(p,": It is HIGHER.", (4-number_guesses)-1, "Guesses left.\n")
                  elif guess_number > secret_number:
                      print(p,": It is LOWER.", (4-number_guesses)-1, "Guesses left.\n")

                  else:
                       print("WAHOOOOOO!!!!!!!!! YOU GOT IT, LEVEL TWO(2) COMPLETED")
                       print("WELCOME TO LEVEL THREE(3), YOU HAVE THREE ATTEMPS. WISH YOU LUCK ")
                       secret_number = randint(1,39) #random number between 1 and 39
                       for number_guesses in range(3): #you only have 3 attempts, one at a time 
                             guess_number = eval(input("Please Enter Your Guess Number Between 1 and 39 (1-39), Press Enter key to Continue: "))
                             if guess_number < secret_number:
                                  print(p,": It is HIGHER.", (3-number_guesses)-1, "Guesses left.\n")
                             elif guess_number > secret_number:
                                  print(p,": It is LOWER.", (3-number_guesses)-1, "Guesses left.\n")
                             else:
                                  print("WAHOOOOOO!!!!!!!!! YOU GOT IT, LEVEL THREE (3) COMPLETED")
                                  print("WELCOME TO LEVEL FOUR(4), YOU HAVE JUST TWO ATTEMPS. WISH YOU LUCK ")
                                  secret_number = randint(1,12) #random number between 1 and 39
                                  for number_guesses in range(2): #you are to provide 2 numbers, one at a time 
                                      guess_number = eval(input("Pleese Enter Your Guess Number Between 1 and 12 (1-12), Press Enter key to Continue: "))
                                      if guess_number < secret_number:
                                         print(p,": It is HIGHER.", (2-number_guesses)-1, "Guesses left.\n")
                                      elif guess_number > secret_number:
                                          print(p,": It is LOWER.", (2-number_guesses)-1, "Guesses left.\n")
                                      else:
                                           print("WAHOOOOOO!!!!!!!!! YOU GOT IT, LEVEL FOUR(4) COMPLETED")
                                           print("WELCOME TO LEVEL FIVE(5), YOU HAVE JUST ONE ATTEMP. WISH YOU LUCK ")
                                           secret_number = randint(1,5) #random number between 1 and 39
                                           for number_guesses in range(1): #you are to provide 2 numbers, one at a time
                                                   guess_number = eval(input("Pleese Enter Your Guess Number Between 1 and 12 (1-12), Press Enter key to Continue: "))
                                                   if guess_number < secret_number:
                                                       print(p,": It is HIGHER ")
                                                   elif guess_number > secret_number:
                                                       print(p,": It is LOWER ")
                                                   else:
                                                       print("WAHOOOOOO!!!!!!!!! YOU GOT IT, CONGRATULATION",p)
                                                       break
                                           else:
                                                print(" Oh no! You Lose. The Correct Number is : ", secret_number, ".Hope You Enjoy It, Come Back Later For Another Trial")
                                  else:
                                      print(" Oh no! You Lose. The Correct Number is : ", secret_number, ".Hope You Enjoy It, Come Back Later For Another Trial")
                                      break
                       else:
                           print(" Oh no! You Lose. The Correct Number is : ", secret_number, ".Hope You Enjoy It, Come Back Later For Another Trial")
                           break
             
             else:
                 print(" Oh no! You Lose. The Correct Number is :  ", secret_number, ".Hope You Enjoy It, Bome Back Later For Another Trial")
                 break
                 
    else:
        print(" Oh no! You Lose. The Correct Number is : ", secret_number, ".Hope You Enjoy It, Come Back Later For Another Trial")
        
