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

ascii_draw_list=[rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice=random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
  print("You input a invalid number")
else:
  print(f"Your choice:{ascii_draw_list[user_choice]}\nComputer choice{ascii_draw_list[computer_choice]}\n")
  if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You Win!")
  elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("Game Over!")
  else:
    print("It's a draw!")

