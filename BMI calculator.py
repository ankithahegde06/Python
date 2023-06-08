print("--------------Exercise 3 to calculate BMI------------------")
weight=float(input("Please enter your weight in kg:"))
height=float(input("please enter your height in meters:"))
bmi=weight/height**2
if bmi<18.5:
    print(f"your weight is: {weight} kg, your height is: {height} sqmts, your bmi is :{bmi}, you are underweight")
elif bmi<25:
    print(f"your weight is: {weight} kg, your height is: {height} sqmts, your bmi is :{bmi}, you BMI is normal")
elif bmi<30:
    print(f"your weight is: {weight} kg, your height is: {height} sqmts, your bmi is :{bmi}, you are over weight")
elif bmi<35:
    print(f"your weight is: {weight} kg, your height is: {height} sqmts, your bmi is :{bmi}, you are obese")
else:
    print(f"your weight is: {weight} kg, your height is: {height} sqmts, your bmi is :{bmi}, you are clinically obese")
