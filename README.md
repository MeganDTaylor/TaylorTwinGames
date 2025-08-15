# Taylor Twin Games

Taylor Twin Games consists of 2 version of the same games. Version 1 runs an interface through your terminal. Version 2 is a Python Tkinter-based desktop application that serves as a launcher for multiple mini-games. The included games are:

- **Hangman**
- **Battleship**
- **Guessing Game**
- **Mastermind**

---

## 🖥️ Requirements

- **Python 3.x**
- **Tkinter** (usually included with Python installations) (for Version 2)
- The following game modules must exist in the same directory:
  - `Hangman.py` (contains `Hangman` class)
  - `Battleship.py` (contains `Battleship` class)
  - `Mastermind.py` (contains `Master_Mind` class)
  - `GuessingGame.py` (contains `GuessingGame` class)

---

## 🚀 How to Run

1. Clone or download the repository.
2. Ensure all required game files (`Hangman.py`, `Battleship.py`, etc.) are in the same folder as `MainGUI.py`.
3. Run the launcher:

```bash
python MainGUI.py
```

## 🎨 GUI Design

Background color: Teal (#00BE99)

Buttons:

Hangman → Light green (#73FF64)

Battleship → Blue (#1400C8)

Guessing Game → Red (#FF0000)

Mastermind → Orange (#FFA600)
