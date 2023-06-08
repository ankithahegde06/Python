name=input("please enter your name: ")
print(f"Welcome {name} to Treasure Island. Your mission is to find the treasure.")
leftOrRight=input("Please choose you want go left or right.")

if leftOrRight=='right':
    print("You fell into fire pit. Game Over!!!")
else:
    swimorwait=input("Do you want swim or wait?")
    if swimorwait=='swim':
        print("you are surrounded by shark. game Over!!!")
    else:
        door=input("Which door do you want take Red,Yellow or Blue?").lower()
        if door=='yellow':
            print("Congratulations!!You found the treasure.")
        else:
            print("you feel into hole. Game Over!!!")