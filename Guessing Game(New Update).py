import tkinter as tk
from tkinter import messagebox
import datetime
from random import randint
import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('guessing_game.db')
cursor = conn.cursor()

# Create the game_progress table
cursor.execute('''
CREATE TABLE IF NOT EXISTS game_progress (
    player_name TEXT,
    level INTEGER,
    attempts_left INTEGER
)
''')
conn.commit()
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
# Main application window
root = tk.Tk()
root.title("Guessing Game")
root.geometry("400x300")

# Variables
player_name_var = tk.StringVar()
guess_number_var = tk.IntVar()
message_var = tk.StringVar()
level = 1
attempts_left = 5
secret_number = randint(1, 39)
def start_game():
    global player_name, level, attempts_left, secret_number
    player_name = player_name_var.get().upper()
    level, attempts_left = load_progress(player_name)
    secret_number = randint(1, 39)
    message_var.set(f"Welcome, {player_name}! Level {level}. You have {attempts_left} attempts.")
    update_ui()

def make_guess():
    global level, attempts_left, secret_number
    guess_number = guess_number_var.get()
    if guess_number < secret_number:
        message_var.set(f"HIGHER. {attempts_left-1} attempts left.")
    elif guess_number > secret_number:
        message_var.set(f"LOWER. {attempts_left-1} attempts left.")
    else:
        level += 1
        message_var.set(f"Congratulations {player_name}, you completed level {level-1}!")
        if level > 5:
            message_var.set(f"Congratulations {player_name}, you have completed all levels!")
        else:
            attempts_left -= 1
            secret_number = randint(1, 39)
            save_progress(player_name, level, attempts_left)
    attempts_left -= 1
    if attempts_left <= 0:
        message_var.set(f"Game over! The secret number was {secret_number}.")
    update_ui()

def update_ui():
    guess_number_var.set(0)
    guess_entry.config(state='normal' if attempts_left > 0 else 'disabled')
    guess_button.config(state='normal' if attempts_left > 0 else 'disabled')

# Create UI elements
tk.Label(root, text="Player Name:").pack(pady=10)
tk.Entry(root, textvariable=player_name_var).pack(pady=10)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

tk.Label(root, textvariable=message_var).pack(pady=10)
tk.Label(root, text="Enter Your Guess:").pack(pady=10)
guess_entry = tk.Entry(root, textvariable=guess_number_var)
guess_entry.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", command=make_guess)
guess_button.pack(pady=10)

# Run the main loop
root.mainloop()
