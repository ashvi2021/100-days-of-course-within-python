height = float(input("enter your height in cm"))
weight = float(input("enter your weight in kg"))
bmi = round(weight / height ** 2)
if bmi < 18:
    print(f"you are under weight. Your BMI is {bmi}")
elif bmi < 25:
    print(f"you have a normal weight. Your BMI is {bmi}")
elif bmi < 30:
    print(f"you are over weight. Your BMI is {bmi}")
elif bmi < 35:
    print(f"you are obese. Your BMI is {bmi}")
else:
    print(f"you are clinically obses. Your BMI is {bmi}")
  
