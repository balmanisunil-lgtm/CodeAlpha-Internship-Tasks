
import random

# Predefined words
words = ["1", "2", "3", "4", "5"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 wrong guesses allowed.")

# Main game loop
while wrong_guesses < max_guesses:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses)
    print("Remaining chances:", max_guesses - wrong_guesses)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You WIN!")
        break

    # Take user input
    guess = input("Guess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Check losing condition
if not all(letter in guessed_letters for letter in secret_word):
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
