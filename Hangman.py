import random

def select_random_word():
    words = ["python", "programming", "developer", "internship", "hangman", "codealpha", "project"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    return displayed

def hangman_game():
    print("Welcome to Hangman Game!")
    word_to_guess = select_random_word()
    guessed_letters = set()
    attempts_remaining = 6

    while attempts_remaining > 0:
        print("\nWord to guess: ", display_word(word_to_guess, guessed_letters))
        print(f"Attempts remaining: {attempts_remaining}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good job! That letter is in the word.")
            if all(letter in guessed_letters for letter in word_to_guess):
                print("\nCongratulations! You guessed the word:", word_to_guess)
                break
        else:
            print("Oops! That letter is not in the word.")
            attempts_remaining -= 1

    if attempts_remaining == 0:
        print("\nGame over! You ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman_game()
