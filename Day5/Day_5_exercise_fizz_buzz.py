print("Welcome to fizz buzz")
number=int(input("Enter the number:-"))
for i in range (0,number):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)
