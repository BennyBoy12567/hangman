import random

word_list = ["Apple", "Banana", "Grapes", "Strawberry", "Mango"]
print(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = [""] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Updates the word_guessed with the correct guesses
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
                    self.num_letters -= 1
                
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")
                

    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            guess = guess.lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter.")

            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            

hangman_game = Hangman(word_list)
hangman_game.ask_for_input()







    



