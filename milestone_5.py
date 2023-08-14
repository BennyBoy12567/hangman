import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = ""
        self.word_guessed = []
        self.num_letters = 0
        self.list_of_guesses = []

    def choose_random_word(self):
        self.word = random.choice(self.word_list).lower()  # Convert word to lowercase
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")
            if self.num_lives == 0:
                print(f"You lost!. The word was '{self.word}'. Better luck next time.")

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
            print("Word to be guessed:", ' '.join(self.word_guessed))
            
            if self.num_letters == 0:
                print("Congratulations. You won the game!")
                break
            elif self.num_lives == 0:
                print(f"Sorry, you ran out of lives. The word was '{self.word}'. Better luck next time.")
                break

    def play_game(self):
        self.choose_random_word()

        while self.num_lives > 0 and self.num_letters > 0:
            self.ask_for_input()

        if self.num_lives > 0:
            print("Congratulations. You won the game!")
        else:
            print(f"You lost!")

if __name__ == "__main__":
    word_list = ["Apple", "Banana", "Grapes", "Strawberry", "Mango"]
    game = Hangman(word_list)
    game.play_game()



