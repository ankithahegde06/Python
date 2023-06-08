import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rockpaperscissor=[rock,paper,scissors]

userchoice=int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

print(f"you choose {rockpaperscissor[userchoice]}")
comp_choice=random.randint(0,len(rockpaperscissor)-1)
print(f"computer choose {rockpaperscissor[comp_choice]}")

if userchoice==comp_choice:
    print("Its a draw!! try again")
elif userchoice==0 and comp_choice==1:
    print("you loose")
elif userchoice==0 and comp_choice==2:
    print("you win")
elif userchoice==1 and comp_choice==0:
    print("you win")
elif userchoice==1 and comp_choice==2:
    print("you loose")
elif userchoice==2 and comp_choice==0:
    print("you loose")
elif userchoice==2 and comp_choice==1:
    print("you win")



