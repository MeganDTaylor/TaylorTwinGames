from tkinter import  Toplevel, Menu, Message, Button
from random import randint

class Battleship():
	def __init__(self):
		self.frame = Toplevel()
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
		self.board = []
		self.random_row = 0
		self.random_col = 0
		self.turn = 0
		self.ship_row = 0
		self.ship_col = 0
		self.create_board()
		self.ship_row = randint(1, 5)
		self.ship_col = randint(0,4)
				
		#def missed(self):
	def give_directions(self):
		try:
			self.directions.deiconify()
		except Exception:
			self.directions = Toplevel()
			self.directions.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
		for widget in self.directions.winfo_children():
			widget.destroy()
		self.directions_give = Message(self.directions, text = "You have 6 changes to guess the correct location of the battleship\nMake a choice be selecting a tile.", width = 1000, pady = 200, font = ("Edwardian Script ITC", 30))
		self.directions_give.pack()
		self.moveon = Button(self.directions, text = "continue", width = 40, command = lambda: self.directions.withdraw())
		self.moveon.pack()
	def create_board(self):
		self.welcome = Message(self.frame, text = "Battleship", width = 500, font = ("parchment", 60))
		self.welcome.grid(row = 0, column = 0, columnspan = 4)
		#Row 1
		self.displayturn = Message(self.frame, text = str(self.turn), font = ("parchment", 50))
		self.displayturn.grid(row = 0, column = 3, columnspan = 2)
		self.oneone = Button(self.frame, text = '', width = 2, height = 1, command = lambda: self.play_game(1,0), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.oneone.grid(row = 1,column = 0)
		self.onetwo = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(1,1), bg = "#%02x%02x%02x" % (18,29,115),font = ("webdings", 20))
		self.onetwo.grid(row = 1,column = 1)
		self.onethree = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(1,2), bg = "#%02x%02x%02x" % (18,29,115),font = ("webdings", 20))
		self.onethree.grid(row = 1,column = 2)
		self.onefour = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(1,3), bg = "#%02x%02x%02x" % (18,29,115),font = ("webdings", 20))
		self.onefour.grid(row = 1,column = 3)
		self.onefive = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(1,4), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.onefive.grid(row = 1,column = 4)
		#Row 2
		self.twoone = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(2,0), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.twoone.grid(row = 2,column = 0)
		self.twotwo = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(2,1), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.twotwo.grid(row = 2,column = 1)
		self.twothree = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(2,2), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.twothree.grid(row = 2,column = 2)
		self.twofour = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(2,3), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.twofour.grid(row = 2,column = 3)
		self.twofive = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(2,4), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.twofive.grid(row = 2,column = 4)
		#Row 3
		self.threeone = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(3,0), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.threeone.grid(row = 3,column = 0)
		self.threetwo = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(3,1), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.threetwo.grid(row = 3,column = 1)
		self.threethree = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(3,2), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.threethree.grid(row = 3,column = 2)
		self.threefour = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(3,3), bg = "#%02x%02x%02x" % (18,29,111), font = ("webdings", 20))
		self.threefour.grid(row = 3,column = 3)
		self.threefive = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(3,4), bg = "#%02x%02x%02x" % (18,29,111), font = ("webdings", 20))
		self.threefive.grid(row = 3,column = 4)
		#Row 4
		self.fourone = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(4,0), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fourone.grid(row = 4,column = 0)
		self.fourtwo = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(4,1), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fourtwo.grid(row = 4,column = 1)
		self.fourthree = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(4,2), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fourthree.grid(row = 4,column = 2)
		self.fourfour = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(4,3), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fourfour.grid(row = 4,column = 3)
		self.fourfive = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(4,4), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fourfive.grid(row = 4,column = 4)
		#Row 5
		self.fiveone = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(5,0), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fiveone.grid(row = 5,column = 0)
		self.fivetwo = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(5,1), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fivetwo.grid(row = 5,column = 1)
		self.fivethree = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(5,2), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fivethree.grid(row = 5,column = 2)
		self.fivefour = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(5,3), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fivefour.grid(row = 5,column = 3)
		self.fivefive = Button(self.frame, text = "", width = 2, height = 1, command = lambda: self.play_game(5,4), bg = "#%02x%02x%02x" % (18,29,115), font = ("webdings", 20))
		self.fivefive.grid(row = 5,column = 4)
	def play_game(self, row, col):
		if self.turn <= 6:
			print(self.ship_row)
			print(self.ship_col)
			for button in self.frame.grid_slaves():
				if int(button.grid_info()["row"]) == row and int(button.grid_info()["column"]) == col:
					if int(button.grid_info()["row"]) == self.ship_row and int(button.grid_info()["column"]) == self.ship_col:
						button["text"] = "o"						
						button["bg"] = "#%02x%02x%02x" % (255,0,0)
						self.displayturn["text"] = self.turn+1
						self.win = Message(self.frame, text = "You Won!", width = 400, font = ("Edwardian Script ITC", 20))
						self.win.grid(row = 6, column = 1, columnspan = 3)
						self.playagain = Message(self.frame, text = "Do you want to play again?", width = 400, font = ("Edwardian Script ITC", 20))
						self.playagain.grid(row = 7, column = 0, columnspan = 5)	
						self.yes = Button(self.frame, text = "YES", width = 10, command = lambda: self.again())
						self.yes.grid(row = 8, column = 0, columnspan = 3)
						self.no = Button(self.frame, text = "NO", width = 10, command = lambda: self.frame.destroy())
						self.no.grid(row = 8, column = 2, columnspan = 3)
					else:
						button["text"] = "r"
						button["bg"] = "#%02x%02x%02x" % (8,72,27)
						self.turn +=1 
						#self.turn += 1
						self.displayturn["text"] = self.turn
		if self.turn == (6):
			for button in self.frame.grid_slaves():
				if int(button.grid_info()["row"]) == self.ship_row and int(button.grid_info()["column"]) == self.ship_col:
					button["text"] = "o"						
					button["bg"] = "#%02x%02x%02x" % (255,0,0)
			self.lose = Message(self.frame, text = "You Lost!", width = 400, font = ("Edwardian Script ITC", 20))
			self.lose.grid(row = 6, column = 1, columnspan = 3)
			self.playagain = Message(self.frame, text = "Do you want to play again?", width = 400, font = ("Edwardian Script ITC", 20))
			self.playagain.grid(row = 7, column = 0, columnspan = 5)	
			self.yes = Button(self.frame, text = "YES", width = 10, command = lambda: self.again())
			self.yes.grid(row = 8, column = 0, columnspan = 3)
			self.no = Button(self.frame, text = "NO", width = 10, command = lambda: self.frame.destroy())
			self.no.grid(row = 8, column = 2, columnspan = 3)
			
	def again(self):
		self.frame.destroy()
		Battleship()
			
			
			
	