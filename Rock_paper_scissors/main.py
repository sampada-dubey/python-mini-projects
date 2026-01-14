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

game = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
if choice >= 0 and choice <= 2:
    print("You chose - ")
    print(game[choice])
computer_choice = random.randint(0, 2)
print(f"Computer chose - ")
print(game[computer_choice])

if choice >= 3 or choice < 0:
    print("You entered an invalid number. You Lose!!")
elif choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and choice == 2:
    print("You Lose!")
elif choice == 0 and computer_choice == 1:
    print("You Lose!")
elif computer_choice == 0 and choice == 1:
    print("You Win!")
elif computer_choice > choice:
    print("You Lose!")
elif computer_choice == choice:
    print("It's a draw!")
