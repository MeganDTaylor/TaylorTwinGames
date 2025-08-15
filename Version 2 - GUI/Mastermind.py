from random import randint
import operator
from tkinter import Toplevel, Menu, Message, Button, Entry
from tkinter import messagebox
	
class Master_Mind:
	def __init__(self):
		self.frame = Toplevel()
		self.frame.iconbitmap("Games\icecreamicon.ico")
		self.frame.withdraw()
		self.directions = Toplevel()
		self.directions.iconbitmap("Games\icecreamicon.ico")
		self.directions.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
		self.directions.withdraw()
		self.num_guesses = Toplevel(self.frame, bg = "#%02x%02x%02x" % (255, 166, 0), pady = 100)
		self.num_guesses.iconbitmap("Games\icecreamicon.ico")
		menu = Menu(self.num_guesses)
		menu.add_command(label = "Quit", command = lambda: quit())
		menu.add_command(label = "Menu", command = lambda: self.num_guesses.destroy())
		menu.add_command(label = "Directions", command = lambda: self.give_directions())
		self.num_guesses.config(menu = menu)
		self.num_guesses.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
		
		self.mastermind = Message(self.num_guesses, text = 'Mastermind', font = ('courier', 50), width = 1000, pady = 10, bg = "#%02x%02x%02x" % (255, 166, 0))
		self.mastermind.pack()
		question = Message(self.num_guesses, text = 'What length would you like to guess?', font = ('courier', 20), width = 1000, pady = 10, bg = "#%02x%02x%02x" % (255, 166, 0))
		question.pack()
		
		self.board = ['|','|']
		self.game = []
		self.count = 0
		self.guess = ''
		self.exact_count = 0
		self.close_count = 0
		self.exact_indexes = []
		self.game_copy = self.game[:]
		
		self.num = Entry(self.num_guesses)
		self.num.focus_set()
		self.num.pack()
		self.num.bind("<Return>", self.check)
		self.num.pack()
	def give_directions(self):
		try:
			self.directions.deiconify()
		except Exception:
			self.directions = Toplevel()
			self.directions.iconbitmap("Games\icecreamicon.ico")
			self.directions.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
		for widget in self.directions.winfo_children():
			widget.destroy()
		self.directions_give = Message(self.directions, text = "Pick a length you want to guess from, then guess the random order of numbers.\nThe numbers may repeat and they go from 1 to 6.", width = 1000, pady = 200, font = ('courier', 20))
		self.directions_give.pack()
		self.moveon = Button(self.directions, text = "continue", width = 40, command = lambda: self.directions.withdraw())
		self.moveon.pack()
	
	def check(self, n):
		try:
			if int(self.num.get()) <= 6 or int(self.num.get() > 0):
				for k in range(int(self.num.get())):
					self.game += [str(randint(1,6))]	
		except Exception:
			messagebox.showwarning("Invalid Entry", "Please try again.")
			try:
				self.num_guesses.destroy()
				Master_Mind()
			except Exception:
				pass
		self.get_guess()
	
	def __str__(self):
		return ''.join(self.board)
	
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
			#self.Record_Score()
			#self.print_score()
			for widget in self.gameboard.winfo_children():
				widget.destroy()
			menu = Menu(self.gameboard)
			menu.add_command(label = "Quit", command = lambda: quit())
			menu.add_command(label = "Menu", command = lambda: self.gameboard.destroy())
			self.gameboard.config(menu = menu)
			self.mastermind = Message(self.gameboard, text = 'Mastermind', font = ('courier', 50), width = 1000, pady = 10, bg = "#%02x%02x%02x" % (255, 166, 0))
			self.mastermind.pack()
			self.win = Message(self.gameboard, text = 'YOU WON!', bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier', 40), width = 1000)
			printword2 = Message(self.gameboard, text = 'The correct sequence was %s' %(''.join(self.board)), width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier',20))
			self.win.pack()
			printword2.pack()
			self.Record_Score()
			
		elif self.count == 20:
			#self.Record_Score()
			#self.print_score()
			for widget in self.gameboard.winfo_children():
				widget.destroy()
			self.mastermind = Message(self.gameboard, text = 'Mastermind', font = ('courier', 50), width = 1000, pady = 10, bg = "#%02x%02x%02x" % (255, 166, 0))
			self.mastermind.pack()
			self.lose = Message(self.gameboard, text = 'YOU LOSE!', bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier', 40), width = 1000)
			printword = Message(self.gameboard, text = 'The correct sequence was %s' %(''.join(self.game)), width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier',20))
			self.lose.pack()
			printword.pack()
			self.Record_Score()
		else:
			self.clear_board()
			self.exact_count = 0
			self.close_count = 0
			self.exact_indexes = []
			self.get_guess()
			
	def play_again(self):
		self.playagain = Message(self.gameboard, text = "Do you want to play again?", width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier',20))
		self.playagain.pack()
		self.playagain_yes = Button(self.gameboard, text = "YES", width = 20, command = lambda: self.again())
		self.playagain_no = Button(self.gameboard, text = "NO", width = 20, command = lambda: self.gameboard.destroy())
		self.playagain_yes.pack()
		self.playagain_no.pack()
		
	
	def again(self):
		self.gameboard.destroy()
		Master_Mind()
		
	def add_score(self):
		for element in self.game_copy:
			if element == '.':
				self.exact_count += 1
			elif element == '*':
				self.close_count += 1
	
	def get_guess(self):
		if self.count != 20:
			self.num_guesses.withdraw()
			try:
				if self.gameboard.winfo_children() == 1:
					pass
			except Exception:
				self.gameboard = Toplevel(bg = "#%02x%02x%02x" % (255, 166, 0))
				self.gameboard.iconbitmap("Games\icecreamicon.ico")
				self.gameboard.geometry("%dx%d%+d%+d" % (1200, 600, 250, 125))
				menu = Menu(self.gameboard)
				menu.add_command(label = "Quit", command = lambda: quit())
				menu.add_command(label = "Menu", command = lambda: self.gameboard.destroy())
				self.gameboard.config(menu = menu)
			self.mastermind = Message(self.gameboard, text = 'Mastermind', font = ('courier', 50), width = 1000, pady = 10, bg = "#%02x%02x%02x" % (255, 166, 0))
			self.mastermind.grid(row = 0, column = 0, columnspan = 3)
			self.digits = Message(self.gameboard, text = "Please enter your guess of %s digits." %(self.num.get()), width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier', 20))
			self.digits.grid(row = 1, column = 0, columnspan = 3)
			self.guess = Entry(self.gameboard)
			self.guess.focus_set()
			self.guess.grid(row = 2, column = 0, columnspan = 3)
			self.guess.bind("<Return>", self.process)
		else:
			self.win_lose()
			
	def process(self, n):
		try:
			if int(self.num.get()) != len(self.guess.get()):
				raise IndexError
			for num in list(str(self.guess.get())):
				if int(num) not in range(1, 7):
					raise IndexError
			self.guess = str(self.guess.get())
			self.game_copy = self.game[:]
			for i in range(int(self.num.get())):
				self.board.insert(-1,self.guess[i])
			for i in range(0,int(self.num.get())):
				if self.exactly(i):
					pass
				else:
					self.close(i)
		except IndexError:
			self.get_guess()
			messagebox.showwarning("Invalid Entry", "Number must be in the correct range.")
		except ValueError:
			self.get_guess()
			messagebox.showwarning("Invalid Entry", "The guess must be all numbers!")
		except Exception:
			self.get_guess()
			messagebox.showwarning("Invalid Entry", "Not the right length guess!")
		self.add_score()
		
		if self.board != ['|','|']:
			if self.count < 10:
				self.board_mess = Message(self.gameboard, text = self, width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier', 13))
				self.board_mess.grid(row = self.count+2, column = 5)
				self.score = Message(self.gameboard, text = 'Exactly: %s\tClose: %s' %(self.exact_count, self.close_count), width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier', 10))
				self.score.grid(row = self.count+2, column = 6)
			else:
				self.board_mess = Message(self.gameboard, text = self, width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier', 13))
				self.board_mess.grid(row = self.count-8, column = 7)
				self.score = Message(self.gameboard, text = 'Exactly: %s\tClose: %s\t' %(self.exact_count, self.close_count), width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0), font = ('courier', 10))
				self.score.grid(row = self.count-8, column = 8)
			self.count += 1
		self.win_lose()
		
	
	def Record_Score(self):
		self.highScores = Toplevel(self.gameboard, width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0))
		self.score = self.count + 1
		self.askname = Message(self.highScores, text = "Please enter your name", bg = "#%02x%02x%02x" % (255, 166, 0), width = 500)
		self.askname.pack()
		file1 = open("Games/Name_Score.txt", "r")
		lines = file1.readlines()
		file1.close()
		self.scores = []
		for line in lines:
			print(line)
			try:
				line = line.split("	")
				self.scores.append((int(line[1]), line[0], int(line[2][:-1])))
			except IndexError:
				pass
		
		self.name = Entry(self.highScores)
		self.name.focus_set()
		self.name.pack()
		self.name.bind("<Return>", self.addscore)
		
		
	def addscore(self, n):
		self.scores.append((self.score, self.name.get(), int(self.num.get())))
		self.scores.sort(key = operator.itemgetter(0))
		self.scores.sort(key = operator.itemgetter(2), reverse = True)
		file2 = open(r"Version 1 - Command Prompt\Name_Score.txt", "w")
		for element in self.scores:
			try:
				file2.write(str(element[1]) + "\t" + str(element[0]) + "\t" + str(element[2]) + "\n")
			except IndexError:
				pass
		file2.close()
		self.print_score()
		
	def print_score(self):
		self.yourscore = Message(self.highScores, text = "Your Score:  " + str(self.count + 1), bg = "#%02x%02x%02x" % (255, 166, 0))
		self.yourscore.pack()
		#print("\t\t\t\t\t\t\t\t\t\t\tHIGH SCORES:\tLENGTH:\n\n")
		file = open(r"Version 1 - Command Prompt\Name_Score.txt", "r")
		text = file.readlines()
		i = 0
		for line in text:
			if i <= 10:
				self.highscores1 = Message(self.highScores, text = line, width = 1000, bg = "#%02x%02x%02x" % (255, 166, 0))
				self.highscores1.pack()
			i += 1
		i = 0
		self.play_againbutton = Button(self.highScores, text = "Continue", width = 40, command = lambda: self.function())
		self.play_againbutton.pack()
		
	def function(self):
		self.highScores.destroy()
		self.play_again()