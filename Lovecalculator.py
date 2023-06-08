first_name=input("please enter your name :")
second_name=input("please enter your partner's name :")
first_name_lower=first_name.lower()
second_name_lower=second_name.lower()
comb_name=first_name_lower+second_name_lower
counter=comb_name.count("t")
counter+=comb_name.count("r")
counter+=comb_name.count("u")
counter+=comb_name.count("e")
counter1=comb_name.count("l")
counter1+=comb_name.count("o")
counter1+=comb_name.count("v")
counter1+=comb_name.count("e")
true=str(counter)
love=str(counter1)
truelove=int(true+love)

if truelove<10 or truelove>90:
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove>40 and truelove<50:
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")
