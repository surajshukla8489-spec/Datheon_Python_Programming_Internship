
import random

# Read words from file
with open("words.txt", "r", encoding="utf-8") as file:
    words = [
        word.strip().lower()
        for word in file
        if word.strip().isalpha() and word.strip().isascii()
    ]

# Select a random word
secret_word = random.choice(words)

guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

stages = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("===== HANGMAN GAME =====")

while wrong_guesses < max_attempts:

    print(stages[wrong_guesses])

    display_word = " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:", display_word)
    print("Guessed letters:", sorted(guessed_letters))
    print("Attempts left:", max_attempts - wrong_guesses)

    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
        print("Enter only one English letter!\n")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!\n")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!\n")

        if all(letter in guessed_letters for letter in secret_word):
            print("Word:", secret_word.upper())
            print("Congratulations! You won!")
            break
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

else:
    print(stages[wrong_guesses])
    print("Game Over! You lost.")
    print("The correct word was:", secret_word.upper())
