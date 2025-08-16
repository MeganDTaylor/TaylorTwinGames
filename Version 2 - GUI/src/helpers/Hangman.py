from tkinter import Toplevel, Message, Button, Menu, Entry
from tkinter import messagebox
from random import randint
import os

helpers_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.dirname(helpers_directory)
version2_path = os.path.dirname(src_directory)
img_path = os.path.join(version2_path, "imgs", "icecreamicon.ico")
games_directory = os.path.dirname(version2_path)
common_directory = os.path.join(games_directory, "Common Files")


class Hangman:
    def __init__(self):
        self.frame = Toplevel()
        self.frame.withdraw()
        self.directions = Toplevel()
        self.directions.iconbitmap(img_path)
        self.directions.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
        self.directions.withdraw()
        self.win = ""
        self.lose = ""
        self.board = [
            [" ", " ", "|", "-", "-", "|", " ", " "],
            [" ", " ", "|", " ", " ", " ", " ", " "],
            [" ", " ", "|", " ", " ", " ", " ", " "],
            [" ", " ", "|", " ", " ", " ", " ", " "],
            [" ", "_", "_", "_", "_", "_", "_", " "],
            ["/", " ", " ", " ", " ", " ", " ", "\\"],
        ]
        self.word = []
        self.count = 0
        self.incorrect = []
        self.guess = ""
        self.user_word = ""
        self.category = ""
        self.num = 0
        self.enter_word = ""
        self.num_players()
        self.random_word = ""

    def give_directions(self):
        try:
            self.directions.deiconify()
        except Exception:
            self.directions = Toplevel()
            self.directions.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
        for widget in self.directions.winfo_children():
            widget.destroy()
        self.directions_give = Message(
            self.directions,
            text="Choose whether you want one or two player.\nIf you chose one player, then you will have to \
choose a category to guess from.\nIf you chose two player, have one person choose a word. When they are done, the second person will guess the word\s by guessing \
one letter at a time.",
            width=1000,
            pady=200,
            font=("segoe print", 10),
        )
        self.directions_give.pack()
        self.moveon = Button(
            self.directions,
            text="continue",
            width=40,
            command=lambda: self.directions.withdraw(),
        )
        self.moveon.pack()

    def __str__(self):
        rows = []
        for row in self.board:
            rows += ("".join(row)) + "\n"
        board = "".join(rows)
        return board + "\n" + "".join(self.word)

    def num_players(self):
        self.num_players = Toplevel(
            self.frame, bg="#%02x%02x%02x" % (115, 255, 100), pady=100
        )
        self.num_players.iconbitmap(img_path)
        menu = Menu(self.num_players)
        menu.add_command(label="Quit", command=lambda: quit())
        menu.add_command(label="Menu", command=lambda: self.num_players.destroy())
        menu.add_command(label="Directions", command=lambda: self.give_directions())
        self.num_players.config(menu=menu)
        self.num_players.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
        self.hangman = Message(
            self.num_players,
            text="Hangman",
            font=("segoe print", 50),
            width=1000,
            pady=10,
            bg="#%02x%02x%02x" % (115, 255, 100),
        )
        self.hangman.pack()
        self.players = Message(
            self.num_players,
            text="How many players?",
            width=400,
            pady=10,
            bg="#%02x%02x%02x" % (115, 255, 100),
            font=("segoe print", 20),
        )
        self.players.pack()
        self.oneplayer = Button(
            self.num_players,
            text="1",
            command=lambda: self.choose_players("1"),
            width=20,
            font=("segoe print", 12),
        )
        self.twoplayer = Button(
            self.num_players,
            text="2",
            command=lambda: self.choose_players("2"),
            width=20,
            font=("segoe print", 12),
        )
        self.oneplayer.pack()
        self.twoplayer.pack()

    def choose_players(self, num):
        self.num = num
        for widget in self.num_players.winfo_children():
            widget.destroy()
        menu = Menu(self.num_players)
        menu.add_command(label="Quit", command=lambda: quit())
        menu.add_command(label="Menu", command=lambda: self.num_players.destroy())
        self.num_players.config(menu=menu)

        if num == "1":
            self.choose_set()

        elif num == "2":
            self.hangman = Message(
                self.num_players,
                text="Hangman",
                font=("segoe print", 50),
                width=1000,
                pady=10,
                bg="#%02x%02x%02x" % (115, 255, 100),
            )
            self.hangman.pack()
            self.display = Message(
                self.num_players,
                text="What word would you like to choose?",
                width=1000,
                bg="#%02x%02x%02x" % (115, 255, 100),
                font=("segoe print", 20),
            )
            self.display.pack()
            self.enter_word = Entry(self.num_players)
            self.enter_word.focus_set()
            self.enter_word.pack()
            self.enter_word.bind("<Return>", self.button)
            self.enter_word.pack()

    def button(self, n):
        try:
            self.refresh()
            self.get_guess()
        except Exception:
            pass

    def refresh(self, e=None):
        if self.num == "2":
            self.user_word = self.enter_word.get()
        for letter in self.user_word:
            if letter == " ":
                self.word += ["  "]
            else:
                self.word += ["_ "]
        self.check()

    def check(self):
        try:
            if self.user_word == "":
                raise ValueError
            for letter in self.user_word:
                if letter == (" "):
                    pass
                elif not letter.isalpha():
                    raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Invalid Entry", "Please enter only letters, please."
            )
            try:
                self.num_players.destroy()
            except Exception:
                pass
            Hangman()

    def change_board(self):
        if self.count == 1:
            self.board[1][5] = "O"
        elif self.count == 2:
            self.board[1][4] = "\\"
        elif self.count == 3:
            self.board[1][6] = "/"
        elif self.count == 4:
            self.board[2][6] = "|"
        elif self.count == 5:
            self.board[3][4] = "/"
        elif self.count == 6:
            self.board[3][6] = "\\"

    def get_guess(self):
        self.num_players.withdraw()
        try:
            for widget in self.gameboard.winfo_children():
                widget.destroy()
        except Exception:
            self.gameboard = Toplevel(bg="#%02x%02x%02x" % (115, 255, 100))
            self.gameboard.iconbitmap(img_path)
            self.gameboard.geometry("%dx%d%+d%+d" % (1000, 600, 250, 125))
            menu = Menu(self.gameboard)
            menu.add_command(label="Quit", command=lambda: quit())
            menu.add_command(label="Menu", command=lambda: self.gameboard.destroy())
            self.gameboard.config(menu=menu)
        self.hangman = Message(
            self.gameboard,
            text="Hangman",
            font=("segoe print", 50),
            width=1000,
            pady=0,
            bg="#%02x%02x%02x" % (115, 255, 100),
        )
        self.hangman.pack()
        self.question = Message(
            self.gameboard,
            text="What letter would you like to guess?",
            width=1000,
            bg="#%02x%02x%02x" % (115, 255, 100),
            font=("segoe print", 20),
        )
        self.question.pack()
        self.board_mess = Message(
            self.gameboard,
            text=self,
            width=1000,
            bg="#%02x%02x%02x" % (115, 255, 100),
            font=("segoe print", 15),
        )
        self.board_mess.pack()
        self.incorrect_list = Message(
            self.gameboard,
            text="Incorrect Attempts:\n%s" % (" ".join(self.incorrect).upper()),
            width=1000,
            bg="#%02x%02x%02x" % (115, 255, 100),
            font=("segoe print", 12),
        )
        self.incorrect_list.pack()
        self.guess = Entry(self.gameboard)
        self.guess.focus_set()
        self.guess.pack()
        self.guess.bind("<Return>", self.check_letter)

    def add_letter(self):
        if self.guess.get().lower() in self.user_word.lower():
            for i in range(len(self.user_word)):
                if self.user_word[i].lower() == self.guess.get().lower():
                    self.word[i] = self.guess.get().upper()
        else:
            if (self.guess.get().upper() not in self.incorrect) and (
                self.guess.get().lower() not in self.incorrect
            ):
                self.count += 1
                self.change_board()
                self.incorrect.append(self.guess.get())
        self.win_lose()

    def check_letter(self, enter):
        if len(self.guess.get()) > 1:
            messagebox.showwarning(
                "Invalid Entry", "Please only enter single characters."
            )
            self.get_guess()
        elif self.guess.get() is not None and not self.guess.get().isalpha():
            messagebox.showwarning("Invalid Entry", "Please do not enter numbers Here.")
            self.get_guess()
        else:
            self.add_letter()

    def win_lose(self):
        split = self.user_word.split(" ")
        user_word_new = "  ".join(split)
        for widget in self.gameboard.winfo_children():
            widget.destroy()
        menu = Menu(self.gameboard)
        menu.add_command(label="Quit", command=lambda: quit())
        menu.add_command(label="Menu", command=lambda: self.gameboard.destroy())
        self.gameboard.config(menu=menu)
        self.hangman = Message(
            self.gameboard,
            text="Hangman",
            font=("segoe print", 50),
            width=1000,
            pady=10,
            bg="#%02x%02x%02x" % (115, 255, 100),
        )
        self.hangman.pack()
        if self.count == 7:
            for widget in self.gameboard.winfo_children():
                widget.destroy()
            menu = Menu(self.gameboard)
            menu.add_command(label="Quit", command=lambda: quit())
            menu.add_command(label="Menu", command=lambda: self.gameboard.destroy())
            self.gameboard.config(menu=menu)
            self.lose = Message(
                self.gameboard,
                text="YOU LOSE!",
                bg="#%02x%02x%02x" % (115, 255, 100),
                font=("segoe print", 40),
                width=1000,
            )
            printword = Message(
                self.gameboard,
                text='The word was "%s"' % (self.user_word),
                width=1000,
                bg="#%02x%02x%02x" % (115, 255, 100),
                font=("segoe print", 20),
            )
            self.lose.pack()
            printword.pack()
            self.playagain = Message(
                self.gameboard,
                text="Do you want to play again?",
                width=400,
                bg="#%02x%02x%02x" % (115, 255, 100),
                font=("segoe print", 20),
            )
            self.playagain.pack()
            self.playagain_yes = Button(
                self.gameboard, text="YES", width=20, command=lambda: self.again()
            )
            self.playagain_no = Button(
                self.gameboard,
                text="NO",
                width=20,
                command=lambda: self.gameboard.destroy(),
            )
            self.playagain_yes.pack()
            self.playagain_no.pack()
        elif "".join(self.word).lower() == user_word_new.lower():
            self.win = Message(
                self.gameboard,
                text="YOU WON!",
                bg="#%02x%02x%02x" % (115, 255, 100),
                font=("segoe print", 40),
                width=1000,
            )
            printword2 = Message(
                self.gameboard,
                text='The word was "%s"' % (self.user_word),
                width=1000,
                bg="#%02x%02x%02x" % (115, 255, 100),
                font=("segoe print", 20),
            )
            self.win.pack()
            printword2.pack()
            self.playagain = Message(
                self.gameboard,
                text="Do you want to play again?",
                width=400,
                bg="#%02x%02x%02x" % (115, 255, 100),
                font=("segoe print", 20),
            )
            self.playagain.pack()
            self.playagain_yes = Button(
                self.gameboard, text="YES", width=20, command=lambda: self.again()
            )
            self.playagain_no = Button(
                self.gameboard,
                text="NO",
                width=20,
                command=lambda: self.gameboard.destroy(),
            )
            self.playagain_yes.pack()
            self.playagain_no.pack()
        else:
            self.get_guess()

    def again(self):
        self.gameboard.destroy()
        Hangman()

    def choose_set(self):
        self.hangman = Message(
            self.num_players,
            text="Hangman",
            font=("segoe print", 50),
            width=1000,
            pady=10,
            bg="#%02x%02x%02x" % (115, 255, 100),
        )
        self.hangman.pack()
        self.category = Message(
            self.num_players,
            text="Please select a category",
            width=400,
            pady=10,
            bg="#%02x%02x%02x" % (115, 255, 100),
            font=("segoe print", 20),
        )
        self.category.pack()
        self.STEM = Button(
            self.num_players,
            text="Stem",
            command=lambda: self.two_commands("1"),
            width=20,
            font=("segoe print", 8),
        )
        self.HISTORY = Button(
            self.num_players,
            text="History",
            command=lambda: self.two_commands("2"),
            width=20,
            font=("segoe print", 8),
        )
        self.MUSIC = Button(
            self.num_players,
            text="Music",
            command=lambda: self.two_commands("3"),
            width=20,
            font=("segoe print", 8),
        )
        self.WORD_OF_THE_DAY = Button(
            self.num_players,
            text="Word of the Day",
            command=lambda: self.two_commands("4"),
            width=20,
            font=("segoe print", 8),
        )
        self.RANDOM = Button(
            self.num_players,
            text="Random",
            command=lambda: self.two_commands("5"),
            width=20,
            font=("segoe print", 8),
        )
        self.STEM.pack()
        self.HISTORY.pack()
        self.MUSIC.pack()
        self.WORD_OF_THE_DAY.pack()
        self.RANDOM.pack()

    def two_commands(self, n):
        self.get_word(n)
        self.get_guess()

    def get_word(self, num):
        file = open(rf"{common_directory}\Hangman_Words\{num}.txt")
        words = []
        lines = file.readlines()
        for line in lines:
            words.append(line[:-1])
        file.close()
        self.random_word = words[randint(0, len(words) - 1)]
        self.user_word = self.random_word
        self.refresh()
