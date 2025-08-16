from random import randint
import os

helpers_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.dirname(helpers_directory)
version1_path = os.path.dirname(src_directory)
logs_highscore_path = os.path.join(version1_path, "logs", "High_Score.txt")


def clear():
    os.system("cls")


class Guessing_Game:
    def __init__(self):
        self.random = []
        self.max_number = 100
        self.random_number = randint(1, self.max_number)
        self.turn = 0
        self.guess_number = 0
        self.high_score = 0

    def welcome(self):
        print(
            '\n\
					  \\____     _   _ U _____ u ____    ____                  _   _     ____         ____      _      __  __  U _____ u  _    \n\
					U /"___|uU |"|u| |\\| ___"|// __"| u/ __"| u      ___     | \\ |"| U /"___|u    U /"___|uU  /"\\  uU|\' \\/ \'|u\\| ___"|/U|"|u  \n\
					\\| |  _ / \\| |\\| | |  _|" <\\___ \\/<\\___ \/      |_"_|   <|  \\| |>\\| |  _ /    \\| |  _ / \\/ _ \/ \\| |\\/| |/ |  _|"  \\| |/  \n\
					 | |_| |   | |_| | | |___  u___) | u___) |       | |    U| |\\  |u | |_| |      | |_| |  / ___ \\  | |  | |  | |___   |_|   \n\
					  \\____|  <<\\___/  |_____| |____/>>|____/>>    U/| |\\u   |_| \\_|   \____|       \\____| /_/   \\_\\ |_|  |_|  |_____|  (_)   \n\
					  _)(|_  (__) )(   <<   >>  )(  (__))(  (__).-,_|___|_,-.||   \\,-._)(|_        _)(|_   \\    >><<,-,,-.   <<   >>  |||_  \n\
					 (__)__)     (__) (__) (__)(__)    (__)      \\_)-\' \'-(_/ (_")  (_/(__)__)      (__)__) (__)  (__)(./  \.) (__) (__)(__)_) \n\
					\n\
					\n\
					This is a guessing game. Guess the random number between 1 and 100! You have as many guesses as you need,\n\t\t\t\t\tbut try to get it in as few guesses as you can!\n'
        )

    def play_game(self):
        self.welcome()
        file = open(logs_highscore_path, "r")
        self.high_score = file.read()
        file.close()
        print("\t\t\t\t\t\t\t\t\t\t\tBest Score: ", self.high_score)
        while True:
            while True:
                try:
                    self.guess_number = int(
                        (input("\t\t\t\t\t\t\t\t\t\t\tPlease enter a number: "))
                    )
                    if self.guess_number < 0 or self.guess_number > self.max_number:
                        raise IndexError
                except ValueError:
                    print(
                        "\t\t\t\t\t\t\t\t\t\t\tLetters are not in the numbering system!"
                    )
                except IndexError:
                    print("\t\t\t\t\t\t\t\t\t\t\tThats not in the range!")
                else:
                    break

            if int(self.random_number) == int(self.guess_number):
                self.turn += 1
                print(
                    "\t\t\t\t\t\t\t\t\t\t\tThat is correct!, your score is ", self.turn
                )
                if (self.turn < int(self.high_score)) or (int(self.high_score) == 0):
                    print("\t\t\t\t\t\t\t\t\t\t\tBest Score!")
                    self.high_score = self.turn
                    file = open(logs_highscore_path, "w")
                    file.write(str(self.high_score))
                    file.close()
                return
            elif self.guess_number > self.random_number:
                self.turn += 1
                print("\t\t\t\t\t\t\t\t\t\t\tToo high!")

            elif self.guess_number < self.random_number:
                self.turn += 1
                print("\t\t\t\t\t\t\t\t\t\t\tToo low!")
