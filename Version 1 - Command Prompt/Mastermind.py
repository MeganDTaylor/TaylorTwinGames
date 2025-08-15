from random import randint
import os
import operator


def clear():
	os.system('cls')

	
class Master_Mind:
	def __init__(self):
		while True:
			try:
				clear()
				self.print_Mastermind()
				self.num = int(input('\t\t\t\t\t\t\t\t\t\t\tWhat length would you like to guess\n\n\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t\t'))
				if self.num > 6 or self.num <= 0:
					raise ValueError
			except ValueError:
				print("\t\t\t\t\t\t\t\t\t\t\tMust be between 1 and 6, and connot be letters!") 
				input("\t\t\t\t\t\t\t\t\t\t\tPress ENTER to continue.")
			else:
				break
		self.board = ['|','|']
		self.game = []
		for k in range(self.num):
			self.game += [str(randint(1,6))]
		self.count = 0
		self.guess = ''
		self.exact_count = 0
		self.close_count = 0
		self.exact_indexes = []
		self.game_copy = self.game[:]
		self.end = True
	def __str__(self):
		return ''.join(self.board)
	def print_Mastermind(self):
		print("\
		\n\n\
\t\t					    _/      _/                        _/                          _/      _/  _/                  _/ \n\
\t\t					   _/_/  _/_/    _/_/_/    _/_/_/  _/_/_/_/    _/_/    _/  _/_/  _/_/  _/_/      _/_/_/      _/_/_/   \n\
\t\t					  _/  _/  _/  _/    _/  _/_/        _/      _/_/_/_/  _/_/      _/  _/  _/  _/  _/    _/  _/    _/ \n\
\t\t					 _/      _/  _/    _/      _/_/    _/      _/        _/        _/      _/  _/  _/    _/  _/    _/      \n\
\t\t					_/      _/    _/_/_/  _/_/_/        _/_/    _/_/_/  _/        _/      _/  _/  _/    _/    _/_/_/     \n\
					\n\
					\n\
					\n")
	def exactly(self,i):
		if int(self.guess[i]) == int(self.game[i]):
			self.game_copy[i] = '.'
			return True
		else:
			return False
	def close(self,i):
		if self.guess[i] in self.game_copy:
			for j in range(len(self.game_copy)):
				if self.game_copy[j] == self.guess[i]:
					self.game_copy[j] = '*'
					break
			return True
		else:
			return False
	def clear_board(self):
		self.board = ['|','|']
		
	def win_lose(self):
		if ('|%s|'%(''.join(self.game))) == (''.join(self.board)):
			print('\n\n\t\t\t\t\t\t\t\t\t\t\tYOU WIN!')
			self.Record_Score()
			self.print_score()
			return True
		else:
			self.count += 1
		if self.count == 20:
			print('\n\t\t\t\t\t\t\t\t\t\t\t |%s| was the correct sequence' %(''.join(self.game)))
			print('\n\n\t\t\t\t\t\t\t\t\t\t\tYOU LOSE!')
			self.Record_Score()
			self.print_score()
			return
	def add_score(self):
		for element in self.game_copy:
			if element == '.':
				self.exact_count += 1
			elif element == '*':
				self.close_count += 1
	def game_play(self):
		clear()
		self.print_Mastermind()
		print('\t\t\t\t\t\t\t\t\tPlease enter your guess of %s digits, or enter "q" to quit:\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\t\tTRY#:\t\t\tGUESSES:\n' %(self.num))
		for plays in range(20):
			while True:
				try:
					print("\t\t", self.count+1, end='')
					self.guess = (input("\t\t\t"))
					if self.guess == ('q' or 'Q'):
						self.end = False
						break
					if len(str(self.guess)) > self.num or len(str(self.guess)) < self.num:
						raise IndexError
					for num in list(str(self.guess)):
						if int(num) not in range(1, 7):
							raise IndexError
				except IndexError:
					print("\t\t\t\t\t\t\t\t\t\t\t Number must be in the correct range!")
				except ValueError:
					print("\t\t\t\t\t\t\t\t\t\t\t The guess must be all numbers!")
				except Exception:
					print("\t\t\t\t\t\t\t\t\t\t\t Not the right length guess!")
				else:
					break
			if self.end:
				self.guess = str(self.guess)
				self.game_copy = self.game[:]
				for i in range(self.num):
					self.board.insert(-1,self.guess[i])
				for i in range(0,self.num):
					if self.exactly(i):
						pass
					else:
						self.close(i)
				self.add_score()	
				print("\t\t\t\t\t\t\t\t\t\t\t",self, end='\t')
				print('Exactly: %s\tClose: %s' %(self.exact_count, self.close_count))
				if self.win_lose():
					return
				self.clear_board()
				self.exact_count = 0
				self.close_count = 0
				self.exact_indexes = []
			else:
				break
				
	def Record_Score(self):
		score = self.count + 1
		name = input("\n\n\t\t\t\t\t\t\t\t\t\t\tPlease enter your name:\t")
		file1 = open(r"Version 1 - Command Prompt\Name_Score.txt", "r")
		lines = file1.readlines()
		file1.close()
		scores = []
		for line in lines:
			try:
				line = line.split("	")
				scores.append((int(line[1]), line[0], int(line[2][:-1])))
			except IndexError:
				pass
		scores.append((score, name, self.num))
		scores.sort(key = operator.itemgetter(0))
		scores.sort(key = operator.itemgetter(2), reverse = True)
		file2 = open(r"Version 1 - Command Prompt\Name_Score.txt", "w")
		for element in scores:
			try:
				file2.write(str(element[1]) + "\t" + str(element[0]) + "\t" + str(element[2]) + "\n")
			except IndexError:
				pass
		file2.close()
		return
		
	def print_score(self):
		clear()
		self.print_Mastermind()
		print("\t\t\t\t\t\t\t\t\t\t\tYOUR SCORE:\n")
		print("\t\t\t\t\t\t\t\t\t\t\t     " + str(self.count + 1) + "\n")
		print("\t\t\t\t\t\t\t\t\t\t\tHIGH SCORES:\tLENGTH:\n\n")
		file = open(r"Version 1 - Command Prompt\Name_Score.txt", "r")
		text = file.readlines()
		i = 0
		for line in text:
			if i <= 20:
				print("\t\t\t\t\t\t\t\t\t\t\t" + line)
			i += 1
		i = 0
		return