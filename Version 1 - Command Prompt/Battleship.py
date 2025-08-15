from random import randint
import os

def clear():
	os.system('cls')

	
	
class Battleship:
	def __init__(self):
		self.board = []
		self.random_row = 0
		self.random_col = 0
		self.turn = 0
		self.ship_row = 0
		self.ship_col = 0

	def welcome(self):
		print ("\n\
								██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗ \n\
								██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗\n\
								██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║\n\
								██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║\n\
								╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝\n\
								 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝ \n\
																					\n\
								██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ ██╗    \n\
								██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗██║    \n\
								██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝██║    \n\
								██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ ╚═╝    \n\
								██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     ██╗    \n\
								╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝    \n\
																					\n\
							\tAll you have to do is guess the row and column you think the ship is on.\n\
								They both go from 1 to 5!\n\
								Thanks for playing!\n\n\n")
								

	def guess_loc(self):	
		while True:
			print()
			try:
				self.guess_row = int(input("\t\t\t\t\t\t\t\t\t\t\tGuess Row: "))
				if self.guess_row not in range(1,6):
					raise ValueError
				self.guess_col = int(input("\t\t\t\t\t\t\t\t\t\t\tGuess Col: "))
				if self.guess_col not in range(1,6):
					raise ValueError
			except ValueError:
				print ("\n\t\t\t\t\t\t\t\t\t\t\t\t\tOops, that's not even in the ocean.")
				print("\t\t\t\t\t\t\t\t\t\t\t\t\tTry again!")
			except:
				print("\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter a valid number!")
			else:
				break
		return(self.guess_row, self.guess_col)		

	def missed(self):	
		print ("\n\t\t\t\t\t\t\t\t\t\t\tMiss!\n")
		self.board[self.guess_row-1][self.guess_col-1] = "X"
		input("\t\t\t\t\t\t\t\t\t\t\tPress ENTER to continue.")
		
	def create_board(self):
		board = []
		for x in range(5):
			self.board.append(["~"] * 5)
		self.ship_row = randint(1, len(self.board))
		self.ship_col = randint(1, len(self.board[0]))
	
	def print_board(self):
		for row in self.board:
			print("\t\t\t\t\t\t\t\t\t\t\t\t\t", end = "")		
			print(" ".join(row))
			
			
	def play_game(self):
		self.create_board()
		while self.turn <= 6:
			print("\t\t\t\t\t\t\t\t\t\t\t\t\t", self.turn+1)
			self.print_board()
			location = self.guess_loc()
			self.guess_row = location[0]
			self.guess_col = location[1]
			if self.turn == 4:
				clear()
				self.welcome()
				self.board[self.guess_row-1][self.guess_col-1] = "X"
				self.board[self.ship_row-1][self.ship_col-1] = "»«"
				self.print_board()
				print ("\n\t\t\t\t\t\t\t\t\t\t\t\t\tGame Over")
				print("	\t\t\t\t\t\t\t\t\t\t\t\t\tThe ship was on", self.ship_row, self.ship_col)
				self.board = []
				print()
				return
			if self.guess_row == self.ship_row and self.guess_col == self.ship_col:
				print ("\n\t\t\t\t\t\t\t\t\t\t\tCongratulations! You Hit my battleship!")
				return
			elif (self.guess_row  != self.ship_row) or (self.guess_col != self.ship_col):
				self.missed()
				self.turn += 1
				clear()
				self.welcome()
				
	