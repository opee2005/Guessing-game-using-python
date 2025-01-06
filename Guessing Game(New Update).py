import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('guessing_game.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store player progress
cursor.execute('''
CREATE TABLE IF NOT EXISTS game_progress (
    player_name TEXT,
    level INTEGER,
    attempts_left INTEGER
)
''')

# Commit the changes and close the connection
conn.commit()

import datetime
from random import *
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('guessing_game.db')
cursor = conn.cursor()

today = datetime.datetime.now()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)
print("WELCOME TO GUESSING GAME, ITS A FIVE(5) STAGES GAME")
print("AS YOU ADVANCE TO NEXT STAGE THE HARDER IT BECOMES")
print("GAME STARTS NOW..... ")

def save_progress(player, level, attempts_left):
    cursor.execute('''
    INSERT INTO game_progress (player_name, level, attempts_left)
    VALUES (?, ?, ?)
    ON CONFLICT(player_name) DO UPDATE SET level=?, attempts_left=?
    ''', (player, level, attempts_left, level, attempts_left))
    conn.commit()

def load_progress(player):
    cursor.execute('SELECT level, attempts_left FROM game_progress WHERE player_name=?', (player,))
    result = cursor.fetchone()
    return result if result else (1, 5)

player_names = []
number_player = int(input("Number of Players: "))
for i in range(number_player):
    Name = input("Player's Name: ")
    Name = Name.upper()
    player_names.append(Name)

shuffle(player_names)
for player in player_names:
    level, attempts_left = load_progress(player)
    print(f"WELCOME {player}, GET IT RIGHT AND MOVE TO THE NEXT LEVEL. YOU HAVE {attempts_left} ATTEMPTS, WISH YOU LUCK")

    secret_number = randint(1, 39)
    for number_guesses in range(attempts_left):
        guess_number = int(input("Please Enter Your Guess Number Between 1 and 39: "))
        if guess_number < secret_number:
            print(f"{player}: It is HIGHER. {attempts_left - number_guesses - 1} Guesses Left.\n")
        elif guess_number > secret_number:
            print(f"{player}: It is LOWER. {attempts_left - number_guesses - 1} Guesses Left.\n")
        else:
            print(f"WAHOOOOOO!!!!!!!!! YOU GOT IT, LEVEL {level} COMPLETED")
            level += 1
            attempts_left -= 1
            save_progress(player, level, attempts_left)
            break
    else:
        print(f"Oh no! You Lose. The Correct Number was: {secret_number}. Hope You Enjoyed It, Come Back Later For Another Trial")
    
# Close the database connection at the end of the game
conn.close()
