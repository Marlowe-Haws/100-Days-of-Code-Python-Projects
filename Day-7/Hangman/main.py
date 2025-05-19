import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
game_over = False
correct_letters = []
incorrect_guesses = []
print(logo)
print("\n Welcome to Hangman!\n")
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

while not game_over:
    display = ""
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if len(guess) > 1:
        print("You typed multiple characters. Please enter a single letter.")
        continue
    if not guess.isalpha():
        print("You typed an invalid character. Please enter a single letter.")
        continue

    if guess in correct_letters or guess in incorrect_guesses:
        print(f"You've already guessed {guess}. Try again.")
        continue

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        incorrect_guesses.append(guess)
        letters_not_in_word = ",".join(incorrect_guesses)
        print(f"Letters not in word: {letters_not_in_word}")
        if lives == 0:
            game_over = True
            print(f"The correct word was {chosen_word}.\n***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
