import random
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
print("You entered:", guess)
