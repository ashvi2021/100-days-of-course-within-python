#Password Generator Project
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','(',')','+','-']
print("welcome to password generator")
nletters = int(input("Enter no of letters you want:-\n"))
no_numbers= int(input(f"Enter no of numbers you want:-\n"))
no_symbol= int(input(f"Enter no of symbol you want:-\n"))
password = ""
#easypassword
for char in range(1, nletters  +1):
    password+= random.choice(letters)
    
for char in range(1, no_numbers +1):
    password+=random.choice(numbers)
    
for char in range(1, no_symbol +1):
    password+= random.choice(symbol)
    
print("Easy Password :-",password)

#hardpassword
password_list=[]

for char in range(1, nletters  +1):
    password_list+= random.choice(letters)
    
for char in range(1, no_numbers +1):
    password_list+=random.choice(numbers)
    
for char in range(1, no_symbol +1):
    password_list+= random.choice(symbol)
    
print(password_list)
random.shuffle(password_list)
print("Hard Password :-",password_list)


                 

