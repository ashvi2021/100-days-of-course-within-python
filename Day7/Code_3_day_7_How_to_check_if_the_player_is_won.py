print("How to check if the player is won")
list = ["aashvi", "kirti", "riya", "pragya", "vyashanvi"]
import random
chosen_word = random.choice(list)
display = []
wordlen = len(chosen_word)
for _ in range (wordlen):
    display+="_"

end_of_game = False
while not end_of_game:    
            guess = input("Guess a letter:-").lower()
            for position in range (wordlen):
                letter = chosen_word[position]
                print(f"Current position: {position} \n Current letter: {letter} \n Guess letter {guess}")
                if letter == guess:
                    display[position] = letter

            print(display)    

if "_" not in display:
    end_of_game = True
    print("You Won")
