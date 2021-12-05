print("rock-paper-scissors")
import random
user_choice=int(input("What do you chosse? Type 0 for rock, 1 for paper, 2 for scissor. \n"))
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")
if user_choice ==0 and computer_choice == 2:
    print("you wins!")
elif computer_choice == 0 and user_choice ==2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice> computer_choice:
    print("you win!")
elif  computer_choice == user_choice:
    print("It's a draw")
elif user_choice >=3 or user_choice <0 :
    print("You typed an invalid nuber, you lose!")
    

