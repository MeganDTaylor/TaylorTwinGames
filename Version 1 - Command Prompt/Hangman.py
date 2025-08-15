from random import randint
import os

def clear():
	os.system('cls')
	
class Hangman:
	def __init__(self):
		self.board = [[' ',' ','|','-','-','|',' ',' '], \
					[' ',' ','|',' ',' ',' ',' ',' '], \
					[' ',' ','|',' ',' ',' ',' ',' '], \
					[' ',' ','|',' ',' ',' ',' ',' '], \
					[' ','_','_','_','_','_','_',' '], \
					['/',' ',' ',' ',' ',' ',' ','\\']]
		self.word = []
		self.count = 0
		self.incorrect = []
		self.user_word = self.get_userword(self.num_players())
		for letter in self.user_word:
			if letter == ' ':
				self.word += ['  ']
			else:
				self.word += ['_ ']
		self.print_board()
		
	def __str__(self):
		rows = []
		for row in self.board:
			rows += '\t\t\t\t\t\t\t\t\t\t\t' + (''.join(row)) + '\n'
		board = (''.join(rows))
		
		return '\n' + board +'\n' + '\t\t\t\t\t\t\t\t\t\t' + ''.join(self.word)
	
	def print_Hangman(self):
		return("\n\
							  o         o                                                                               \n\
							 <|>       <|>                                                                              \n\
							 < >       < >                                                                              \n\
							  |         |      o__ __o/  \o__ __o     o__ __o/  \o__ __o__ __o      o__ __o/  \o__ __o  \n\
							  o__/_ _\__o     /v     |    |     |>   /v     |    |     |     |>    /v     |    |     |> \n\
							  |         |    />     / \  / \   / \  />     / \  / \   / \   / \   />     / \  / \   / \ \n\
							 <o>       <o>   \      \o/  \o/   \o/  \      \o/  \o/   \o/   \o/   \      \o/  \o/   \o/ \n\
							  |         |     o      |    |     |    o      |    |     |     |     o      |    |     |  \n\
							 / \       / \    <\__  / \  / \   / \   <\__  < >  / \   / \   / \    <\__  / \  / \   / \ \n\
													|                                           \n\
												o__     o                                           \n\
												<\__ __/>                                           \n\
						\n\
						\n\
							")
		
	def num_players(self):
		while True:
			try:
				print(self.print_Hangman())
				players = str(input('											How many players? 1/2\n\n\t\t\t\t\t\t\t\t\t\t\t\t'))
				if players not in ['1', '2']:
					raise ValueError
				break
			except ValueError:
				print("\t\t\t\t\t\t\t\t\t\t\tPlease select a valid number!")
				input("\t\t\t\t\t\t\t\t\t\t\tPress ENTER to continue.")
				clear()
		return players
	
	def get_userword(self, players):
		if players == '1':
			clear()
			print(self.print_Hangman())
			game_word = self.choose_set()
		elif players == '2':
			clear()
			while True:
				try:
					print(self.print_Hangman())
					game_word = input('											What word would you like to choose?\n\n\t\t\t\t\t\t\t\t\t\t\t\t')
					clear()
					for letter in game_word:
						if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
							raise ValueError
					break
				except ValueError:
					print("\t\t\t\t\t\t\t\t\t\t\tPlease do not have any numbers!")

		return game_word
	
	def print_board(self):
		print("\t\t\t\t\t\t\t\t\t\t", self.print_Hangman())
		print('\n\n\n\t\t\t\t\t\t\t\t\t\t')
		print("\t\t\t\t\t\t\t\t\t\t\t", self)
		print('\n\t\t\t\t\t\t\t\t\t\tIncorrect Attempts:\n\n')
	
	def change_board(self):
		if self.count == 1:
			self.board[1][5] = 'O'
		elif self.count == 2:
			self.board[1][4] = '\\'
		elif self.count == 3:
			self.board[1][6] = '/'
		elif self.count == 4:
			self.board[2][5] = '|'
		elif self.count == 5:
			self.board[3][4] = '/'
		elif self.count == 6:
			self.board[3][6] = '\\'
			
	def is_valid(self, x):
		if x.lower() in self.user_word.lower():
			return True
		else:
			return False
			
	def add_letter(self):
		while True:
			try:
				guess = input("\n\t\t\t\t\t\t\t\t\t\t**********************************\n\t\t\t\t\t\t\t\t\t\tWhat letter do you want to guess?\n\t\t\t\t\t\t\t\t\t\t\t")
				if len(guess) > 1:
					raise ValueError
				if guess in ['1', '2','3','4','5','6','7','8','9','0']:
					raise Exception
				break
			except ValueError:
				clear()
				print("\t\t\t\t\t\t\t\t\t\t", self.print_Hangman())
				print('\n\n\n')
				print("\t\t\t\t\t\t\t\t\t\t", self)
				print('\n\t\t\t\t\t\t\t\t\t\tIncorrect Attempts:')
				print('\n\t\t\t\t\t\t\t\t\t\t' + ' '.join(self.incorrect).upper())
				print("										Please enter a valid character!")
			except Exception:
				clear()
				print("\t\t\t\t\t\t\t\t\t\t", self.print_Hangman())
				print('\n\n\n')
				print("\t\t\t\t\t\t\t\t\t\t", self)
				print('\n\t\t\t\t\t\t\t\t\t\tIncorrect Attempts:')
				print('\n\t\t\t\t\t\t\t\t\t\t' + ' '.join(self.incorrect).upper())
				print("										No Numbers!!")
		
		if self.is_valid(guess):
			for i in range(len(self.user_word)):
				if self.user_word[i].lower() == guess.lower():
					self.word[i] = guess.upper()
		else:
			if (guess.upper() not in self.incorrect) and (guess.lower() not in self.incorrect):
				self.count += 1
				self.change_board()
				self.incorrect.append(guess)
		clear()
		print("\t\t\t\t\t\t\t\t\t\t", self.print_Hangman())
		print('\n\n\n')
		print("\t\t\t\t\t\t\t\t\t\t", self)
		print('\n\t\t\t\t\t\t\t\t\t\tIncorrect Attempts:')
		print('\n\t\t\t\t\t\t\t\t\t\t' + ' '.join(self.incorrect).upper())
		self.win_lose()	
		
	def win_lose(self):
		split = self.user_word.split(' ')
		user_word_new = '  '.join(split)
		if self.count == 7:
			clear()
			print("\t\t\t\t\t\t\t\t\t\t", self.print_Hangman())
			print('\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tYOU LOSE!')
			print('\n\n\t\t\t\t\t\t\t\t\t\t\tThe word was "%s" \n\n' %(self.user_word))
			
		elif ''.join(self.word).lower() == user_word_new.lower():
			clear()
			print(self.print_Hangman())
			print('\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tYOU WON!\n\n')
			print('\t\t\t\t\t\t\t\t\t\t\tThe word was "%s" \n\n' %(self.user_word))
		else:
			self.add_letter()

	def choose_set(self):
		theme_values = {'1': "(1) STEM", '2': "(2) History", '3': "(3) Music", '4': "(4) Word of the day", '5': "(5) Random"}
		clear()
		print(self.print_Hangman())
		print("\t\t\t\t\t\t\t\t\t\tWhat theme would you like to play?\n\t\t\t\t\t\t\t\t\t\tPlease select the number \t\t\t\t\t\t\t\t\t\t")
		print("\t\t\t\t\t\t\t\t\t\tHere are the sets!\n")
		for value in theme_values.values():
			print("\t\t\t\t\t\t\t\t\t\t", value)
		while True:
			try:
				theme_num = (input("\n\t\t\t\t\t\t\t\t\t\t\t\t"))
				if theme_num not in theme_values.keys():
					raise ValueError
				file = open(rf"Version 1 - Command Prompt\{theme_num}.txt")
			except ValueError:
				print("\t\t\t\t\t\t\t\t\t\tPlease select a valid number:).")
			except IOError:
				print("\t\t\t\t\t\t\t\t\t\t\t\tFile under construction\n\t\t\t\t\t\t\t\t\t\t\t\tPlease choose another.")
			else:
				break
		words = []
		lines = file.readlines()
		for line in lines:
			words.append(line[:-1])
		file.close()
		clear()
		return(words[randint(0, len(words)-1)])