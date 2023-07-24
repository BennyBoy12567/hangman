# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

#Milestone_2.py

- Mileston_2.py randomly generates a element from the variable word_list. It also contains a function which asks the user for a single letter input. If more than one letter is selected a error message is printed.
- Using import random which imports the random module we can then use random.choice to randomly select an element from the list word_list. The function get_single_letter_input alows the the user to select only one letter by usinf the == 1 and that it is a letter by using .isalpha. 
```python
   """import random
word_list = ["Apple", "Banana", "Grapes", "Strawberry", "Mango"]
print(word_list)

#selects a random element from the word_list
random = random.choice(word_list)
print(random)

#function to get a sigle letter input
def get_single_letter_imput():
    while True:
        user_input = input("Please enter a single letter: ")
        if len(user_input) == 1 and user_input.isalpha():
            print("Good guess!")
        else:
            print("Oops! That is not a valid input.")
    
guess = get_single_letter_imput()
print("You entered:", guess)"""