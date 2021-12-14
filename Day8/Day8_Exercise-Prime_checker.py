print("Program for prime checker using function")


def prime_check(number):
    is_prime = True
    for i in range(2, number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

        
n= int(input("Enter the Number:-"))
prime_check(number=n)
    
