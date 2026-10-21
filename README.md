# Hangman Game - Python

## Project Description
Hangman is a terminal-based word guessing game developed using Python. The computer randomly selects a secret word from an English word list, and the player must guess the word one letter at a time.

The player gets a maximum of 6 incorrect attempts to guess the word correctly.

## Features
- Random word selection from `words.txt`
- Interactive command-line gameplay
- ASCII gallows art that updates after incorrect guesses
- Maximum of 6 incorrect attempts
- Displays correctly guessed letters
- Prevents duplicate guesses from reducing attempts
- Win and lose messages

## Technologies Used
- Python 3
- random module
- File handling
- Sets and loops
- Conditional statements
- ASCII art

## Project Structure
```text
Hangman_project/
├── hangman.py
├── words.txt
└── README.md
```

## How to Run

1. Install Python 3.
2. Download or clone this project.
3. Make sure `hangman.py` and `words.txt` are in the same folder.
4. Open the terminal in the project folder.
5. Run the following command:

```bash
python hangman.py
```

## How to Play
1. Run the game in the terminal.
2. Enter one English letter at a time.
3. Guess the hidden word before using all 6 incorrect attempts.
4. Repeated guesses do not reduce your attempts.
5. Guess the complete word to win!

## Author
Python Programming Internship Project
