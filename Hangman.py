import random
# List of words for the game (you can expand this list with more words)
word_list = ["python", "hangman", "programming", "computer", "keyboard", "monitor"]

def select_random_word():
    """Selects a random word from the word_list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters and underscores for unguessed letters."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    """Main function to play the Hangman game."""
    print("Welcome to Hangman!")
    word_to_guess = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Adjust this number based on difficulty preference
    
    while True:
        print("\nWord to guess:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Correct!")
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
        
        if incorrect_guesses >= max_incorrect_guesses:
            print("\nSorry, you've run out of guesses!")
            print("The word was:", word_to_guess)
            break
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    # your code here
    hangman()
