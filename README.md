# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone_2.py

- Mileston_2.py randomly generates a element from the variable word_list. It also contains a function which asks the user for a single letter input. If more than one letter is selected a error message is printed.
- Using import random which imports the random module we can then use random.choice to randomly select an element from the list word_list. The function get_single_letter_input alows the the user to select only one letter by usinf the == 1 and that it is a letter by using .isalpha. 

## Milestone_3.py
- The check_guess function takes the guessed letter as an argument and then checks if the letter is in the word. It first convers the guess to lowercase using the .lower method. Then makes sure that the user is only inputing 1 letter. If the letter is in the word it will return the message; "Good guess! {guess} is in the word". We use an else statement if the letter is not in the word. If the users input is invalid with more than 1 letter inputted or a number we print the statement; "Invalid letter. Please, enter a single alphabetical character".
- the ask_for_input function asks the user to guess a letter. We then call the check_guess function to check if the guess is in the word.

## Milestone_4.py
- Creates a hangman class. This class has 2 methods check_guess and ask_for_user_input.
- In summary, the check_guess method takes a guessed letter as input, converts it to lowercase to perform a case-insensitive comparison. If the guessed letter is found in the secret word (self.word).
- In summary, the ask_for_user_input method contains a while loop that runs continuously until the game is won or lost. It repeatedly asks the user to input a letter as their guess. The method then converts the guessed letter to lowercase for consistency.

## Milestone_5.py
- It defines a Hangman class with methods for initializing the game, checking guesses, asking for player input, and playing the game.
- The game starts by selecting a random word from a predefined list of words. The player has a limited number of lives (default 5) to guess the letters of the word correctly.
- The player is prompted to guess a letter. The game validates the input and checks if the letter is present in the chosen word.
- If the guessed letter is correct, the game reveals its position(s) in the word, and the player gets to make another guess.
- If the guessed letter is incorrect, the player loses a life, and the remaining lives are displayed.
- The game continues until the player correctly guesses all the letters of the word or runs out of lives.
- After the game ends, a message is displayed either congratulating the player on winning or revealing the correct word if they lost.





