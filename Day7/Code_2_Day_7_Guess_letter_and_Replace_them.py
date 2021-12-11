print("Program for guessing the letter and replacing blank with that letter")
list = ["aashvi", "kirti", "riya", "pragya", "vyashanvi"]
import random
chosen_word = random.choice(list)
display = []
wordlen = len(chosen_word)
for _ in range (wordlen):
    display+="_"
guess = input("Guess a letter:-").lower()
for position in range (wordlen):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)        
