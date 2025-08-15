from tkinter import  *
from tkinter import messagebox
from random import randint

class GuessingGame():
	def __init__(self):
		self.frame = Toplevel(bg = "#%02x%02x%02x" % (255, 0, 0))
		self.frame.iconbitmap("Games\icecreamicon.ico")
		self.directions = Toplevel()
		self.directions.iconbitmap("Games\icecreamicon.ico")
		self.directions.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
		self.directions.withdraw()
		menu = Menu(self.frame)
		menu.add_command(label = "Quit", command = lambda: quit())
		menu.add_command(label = "Menu", command = lambda: self.frame.destroy())
		menu.add_command(label = "Directions", command = lambda: self.give_directions())
		self.frame.config(menu = menu)
		self.frame.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
		self.random = []
		self.max_number = 100
		self.random_number = randint(1, self.max_number)
		self.turn = -1
		self.guess_number = 0
		self.high_score = 0
		self.get_score()
		self.play_game()
		
	def give_directions(self):
		try:
			self.directions.deiconify()
		except:
			self.directions = Toplevel()
			self.directions.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
		for widget in self.directions.winfo_children():
			widget.destroy()
		self.directions_give = Message(self.directions, text = "You have as many tries as you need to guess the correct number. It lies between 1 and 100.", width = 1000, pady = 200, font = ('century gothic', 30))
		self.directions_give.pack()
		self.moveon = Button(self.directions, text = "continue", width = 40, command = lambda: self.directions.withdraw())
		self.moveon.pack()
		
	def get_score(self):
		file = open("Games/High_Score.txt", "r")
		self.high_score = file.read()
		file.close()
		
	def play_game(self):
		self.turn += 1
		self.welcome = Message(self.frame, text = "Guessing Game", width = 600, font = ('century gothic', 50), bg = "#%02x%02x%02x" % (255, 0, 0))
		self.welcome.grid(row = 0, column = 0, columnspan = 5)
		self.best_score = Message(self.frame, text = "Best Score: %s" %(self.high_score), font = ('century gothic', 15), width = 500, bg = "#%02x%02x%02x" % (255, 0, 0))
		self.best_score.grid(row = 3, column = 4, columnspan = 2)
		self.enter = Message(self.frame, text = "Please enter a number:", width = 400, font = ('century gothic', 20), bg = "#%02x%02x%02x" % (255, 0, 0))
		self.enter.grid(row = 2, column = 0)
		self.guess_number_entry = Entry(self.frame)
		self.guess_number_entry.focus_set()
		self.guess_number_entry.grid(row = 2, column = 3)
		self.guess_number_entry.bind("<Return>", self.check)
		
	def play_again(self):
		self.frame.destroy()
		GuessingGame()
	
	def check(self, n):
		try:
			self.guess_number = self.guess_number_entry.get()
			if int(self.guess_number) < 0 or int(self.guess_number) > self.max_number:
					raise IndexError
		except ValueError:
			messagebox.showwarning("Error", "Letters are not in the numbering system!")
			self.play_game()
		except IndexError:
			messagebox.showwarning("Error", "Thats not in the range!")
			self.play_game()
		if int(self.random_number) == int(self.guess_number):
			self.turn += 1
			self.correct = Message(self.frame, text = "That is correct! Your score is %s" %(self.turn), width = 400, font = ('century gothic', 20), bg = "#%02x%02x%02x" % (255, 0, 0))
			self.correct.grid(row = 4, column = 4, columnspan = 1, rowspan = 2)
			self.status = "Perfect"
			
			self.playagain = Message(self.frame, text = "Do you want to play again?", width = 1000, bg = "#%02x%02x%02x" % (255, 0, 0), font = ('century gothic',20))
			self.playagain.grid(row = 6, column = 4, rowspan = 2)
			self.playagain_yes = Button(self.frame, text = "YES", width = 20, command = lambda: self.play_again(), font = ('century gothic',13))
			self.playagain_no = Button(self.frame, text = "NO", width = 20, command = lambda: self.frame.destroy(), font = ('century gothic',13))
			self.playagain_yes.grid(row = 8, column = 4, rowspan = 2)
			self.playagain_no.grid(row = 10, column = 4, rowspan = 2)
		
			if (self.turn < int(self.high_score)) or (int(self.high_score) == 0):
				self.high_score = self.turn
				file = open("High_Score.txt", "w")
				file.write(str(self.high_score))
				file.close()
		elif int(self.guess_number) > self.random_number:
			self.status = "Too High"
			self.play_game()
		elif int(self.guess_number) < self.random_number:
			self.status = "Too Low"
			self.play_game()
		self.progress = Message(self.frame, text = "%s   Guess: %s   Status: %s"  %(self.turn, self.guess_number, self.status), width = 400, font = ('century gothic', 15), bg = "#%02x%02x%02x" % (255, 0, 0))
		self.progress.grid(row = self.turn+2, column = 0)