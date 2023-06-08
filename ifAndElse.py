print("Welcome to Amusement Park")
height=int(input("Please enter your height :"))
if height>=120:
    print("you can ride the rollacoster")
    age=int(input("Please enter your age :"))
    if age<12:
        print("your ticket price is $5.")
    elif age>=12 and age<18:
        print("your ticket price is $7.")
    elif age>=45 and age<=55:
        print("your ticket price is $0.")
    else:
        print("your ticket price is $12.")
else:
    print("you cannot ride the rollacoster")
