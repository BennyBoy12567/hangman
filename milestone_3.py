import random
word_list = ["Apple", "Banana", "Grapes", "Strawberry", "Mango"]
print(word_list)

#selects a random element from the word_list
word = random.choice(word_list)
print(word)

#takes the guessed letter as an argument and checks if the letter is in the word.
def check_guess(guess):
    #coverts guess to lowercase
    guess = guess.lower()
    if len(guess) == 1 and guess.isalpha():
        if guess in word.lower():
            print(f"Good guess! {guess} is in the word.")
            return True
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    return False


def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if check_guess(guess):
            break

ask_for_input()





