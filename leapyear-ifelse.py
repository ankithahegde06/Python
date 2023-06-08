year=int(input("Please enter the year you want to check if it is a Leap Year :"))
if year%4==0:
    if year%400==0:
        print(f"{year} is a Leap year")
    elif year%100==0:
        print(f"{year} is not a Leap year")
    else:
        print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")
