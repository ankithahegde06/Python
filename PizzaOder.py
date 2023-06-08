print("Welcome to python pizza delivery!!")
size=input("What size pizza do you want? S,M,L :")
add_pepperoni=input("Do you want pepperoni? Y or N")
extra_cheese=input("Do you want extra cheese? Y or N")
bill=0
small=15
medium=20
large=25
total=0
if add_pepperoni=='Y':
    if size=='S':
        bill=2
        print("Pepperoni for small pizza $2")
    if size=='M':
        bill=3
        print("Pepperoni for small pizza $3")
    if size=='L':
        bill=3
        print("Pepperoni for small pizza $3")
if extra_cheese=='Y':
    print("Extra cheese for any size pizza $1")
    bill+=1
if size=='S':
    total=small+bill
    print(f"Your total bill is :{total}")
if size=='M':
    total=medium+bill
    print(f"Your total bill is :{total}")
if size=='L':
    total=large+bill
    print(f"Your total bill is :{total}")


