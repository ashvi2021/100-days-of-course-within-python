print("Program for guessing the letter")
list = ["aashvi", "kirti", "riya", "pragya", "vyashanvi"]
import random
chosen_word = random.choice(list)
guess = input("Guess a letter:-").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
    
