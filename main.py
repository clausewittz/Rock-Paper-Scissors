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

import random
images_list = [rock,paper,scissors]

user_choice = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print("Your choice:")
try:
  print(images_list[user_choice])
except IndexError:
  print("You can't choose below 0 and above 2.")

  
computer_choice = random.randint(0,2)
print(f"Computer choice: {computer_choice}")
print(images_list[computer_choice])

if user_choice < 0 or user_choice > 2:
  print("Invalid number. You lose.")

elif user_choice == 0 and computer_choice == 2:
  print("You win.")
  
elif computer_choice == user_choice:
  print("Draw.")

elif computer_choice == 0 and user_choice == 2:
  print("You lose.")

elif user_choice > computer_choice:
  print("You win.")

elif computer_choice > user_choice:
  print("You lose.")

else:
  print("Invalid number.")
