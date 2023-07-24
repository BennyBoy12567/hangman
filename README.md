# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone_2.py

- Mileston_2.py randomly generates a element from the variable word_list. It also contains a function which asks the user for a single letter input. If more than one letter is selected a error message is printed.
- Using import random which imports the random module we can then use random.choice to randomly select an element from the list word_list. The function get_single_letter_input alows the the user to select only one letter by usinf the == 1 and that it is a letter by using .isalpha. 

## Milestone_3.py
- The check_guess function takes the guessed letter as an argument and then checks if the letter is in the word. It first convers the guess to lowercase using the .lower method. Then makes sure that the user is only inputing 1 letter. If the letter is in the word it will return the message; "Good guess! {guess} is in the word". We use an else statement if the letter is not in the word. If the users input is invalid with more than 1 letter inputted or a number we print the statement; "Invalid letter. Please, enter a single alphabetical character".
- the ask_for_input function asks the user to guess a letter. We then call the check_guess function to check if the guess is in the word.