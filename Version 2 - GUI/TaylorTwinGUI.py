from tkinter import *
from Hangman import Hangman
from Battleship import Battleship
from Mastermind import Master_Mind
from GuessingGame import GuessingGame

class MainGUI:
	def __init__(self, master):
		self.frame = Frame(master, width = 1000, height = 600, pady = 80, bg = "#%02x%02x%02x" % (0, 190, 153))
		menu = Menu(master)
		menu.add_command(label = "Quit", command = lambda: quit())
		master.config(menu = menu)
		self.frame.pack_propagate(0)
		self.frame.pack()
		self.name = Message(self.frame, text = "Taylor Twin Games", width = 1000, pady = 10, bg = "#%02x%02x%02x" % (0, 190, 153), font = ('gabriola', 50))
		self.name.pack()
		self.choose = Message(self.frame, text = "What game would you like to play?", width = 1000, bg = "#%02x%02x%02x" % (0, 190, 153), pady = 0, font = ('gabriola', 20))
		self.choose.pack()
		self.hangman = Button(self.frame, text = "Hangman", command=lambda: Hangman(), width = 20, bg = "#%02x%02x%02x" % (115, 255, 100), font = ('gabriola', 14))
		self.Battleship = Button(self.frame, text = "Battleship", command=lambda: Battleship(), width = 20, bg = "#%02x%02x%02x" % (20, 0, 200), font = ('gabriola', 14))
		self.Guessing_Game = Button(self.frame, text = "Guessing Game", width = 20,command = lambda: GuessingGame(), font = ('gabriola', 14), bg = "#%02x%02x%02x" % (255, 0, 0)) 	
		self.Master_Mind = Button(self.frame, text = "Mastermind", width = 20, bg = "#%02x%02x%02x" % (255, 166, 0), command = lambda: Master_Mind(), font = ('gabriola', 14))
		self.hangman.pack()
		self.Battleship.pack()
		self.Guessing_Game.pack()
		self.Master_Mind.pack()		
			
root = Tk()
root.title("Taylor Twin Games")
root.iconbitmap("Games\icecreamicon.ico")
Games = MainGUI(root)
root.mainloop()
