print("Welcome to the Rollercoster ride")
height = int(input("What is your height in cm"))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age<=18:
        print("Please pay $12")
    else:
        print("Please pay $20")
else:
   print("Sorry, You have to grow taller before you can ride")
    
