from random import randint
import os
from Hangman import Hangman
from Battleship import Battleship
from Mastermind import Master_Mind
from Guessing_Game import Guessing_Game

import sys

def clear():
	os.system('cls')

def print_title():
	print("		\n\
\t\t\t\t\t _______  _______  __   __  ___      _______  ______      _______  _     _  ___   __    _    _______  _______  __   __  _______  _______ \n\
\t\t\t\t\t|       ||   _   ||  | |  ||   |    |       ||    _ |    |       || | _ | ||   | |  |  | |  |       ||   _   ||  |_|  ||       ||       |\n\
\t\t\t\t\t|_     _||  |_|  ||  |_|  ||   |    |   _   ||   | ||    |_     _|| || || ||   | |   |_| |  |    ___||  |_|  ||       ||    ___||  _____|\n\
\t\t\t\t\t  |   |  |       ||       ||   |    |  | |  ||   |_||_     |   |  |       ||   | |       |  |   | __ |       ||       ||   |___ | |_____ \n\
\t\t\t\t\t  |   |  |       ||_     _||   |___ |  |_|  ||    __  |    |   |  |       ||   | |  _    |  |   ||  ||       ||       ||    ___||_____  |\n\
\t\t\t\t\t  |   |  |   _   |  |   |  |       ||       ||   |  | |    |   |  |   _   ||   | | | |   |  |   |_| ||   _   || ||_|| ||   |___  _____| |\n\
\t\t\t\t\t  |___|  |__| |__|  |___|  |_______||_______||___|  |_|    |___|  |__| |__||___| |_|  |__|  |_______||__| |__||_|   |_||_______||_______|\n\
\n\
\n")
	
def play(ans = None):
	print("The Taylor Twins, Version 2.2 (5/5/2018)")
	
	if ans == None:
		while True:
			try:
				print_title()
				ans = input('\n\n											What game would you like to play?\n\n\t\t\t\t\t\t\t\
					(1) Hangman\n\t\t\t\t\t\t\t \
					(2) Battleship\n\t\t\t\t\t\t\t \
					(3) Guessing Game\n\t\t\t\t\t\t\t \
					(4) Master Mind\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t')
				if ans not in ['1','2','3','4']:
					raise ValueError
			except ValueError:
				print("\t\t\t\t\t\t\t\t\t\t\tPlease select a valid number.")
				clear()
			else:
				break
	if ans == '1':
		global id
		id = '1'
		clear()
		board = Hangman()
		board.add_letter()
		play_again()
	elif ans == '2':
		id = '2'
		clear()
		b1 = Battleship()
		b1.welcome()
		b1.play_game()
		play_again()
	elif ans == '3':
		id = '3'
		clear()
		b1 = Guessing_Game()
		b1.play_game()
		play_again()
	elif ans == '4':
		id = '4'
		clear()
		play = Master_Mind()
		play.print_Mastermind()
		play.game_play()
		play_again()
	else:
		print('					Did not work')
	
def play_again():
	while True:
		try:
			game_ans = input('\n\t\t\t\t\t\t\t\t\t\t\tDo you want to play again? y/n\n\n\t\t\t\t\t\t\t\t\t\t\t\t')
			if game_ans == 'y':
				clear()
				play(id)
			elif game_ans == 'n':
				ans = input("					\n\n\t\t\t\t\t\t\t\t\t\t\tDo you want to play another game? (y/n)\n\n\t\t\t\t\t\t\t\t\t\t\t\t")
				if ans == "y":
					clear()
					play()
			if game_ans not in "yn":
				raise ValueError
				
		except ValueError:
			print("\t\t\t\t\t\t\t\t\t\t\tPlease enter a valid response")
		else:
			break
	print("\n\n\t\t\t\t\t\t\t\t\t\t\tThank you for playing!")
	input()
	
clear()		
play()