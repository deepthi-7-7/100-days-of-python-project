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

#Write your code below this line 👇
import random
user_choice=input("Enter what is your choice (rock,paper,scissors)\n")
options=['rock','paper','scissors']
computer_choice=random.choice(options)

if user_choice==computer_choice:
  if user_choice=='rock':
    print("user choice is:\n")
    print(rock)
    print("computer choice is:\n")
    print(rock)
    print("\n You both chose rock. So it's a draw")

  elif user_choice=='paper':
    print("user choice is:\n")
    print(paper)
    print("computer choice is:\n")
    print(paper)
    print("\n You both chose paper. So it's a draw")

  else:
    print("user choice is:\n")
    print(scissors)
    print("computer choice is:\n")
    print(scissors)
    print("\n You both chose scissors. So it's a draw")

elif user_choice=='rock':
  if computer_choice=='paper':
    print("user choice is:\n")
    print(rock)
    print("computer choice is:\n")
    print(paper)
    print("\n Paper defeats rock. So you lost")

  else:
    print("user choice is:\n")
    print(rock)
    print("computer choice is:\n")
    print(scissors)
    print("\n Rock breaks scissors. So you won")

elif user_choice=='paper':
  if computer_choice=='rock':
    print("user choice is:\n")
    print(paper)
    print("computer choice is:\n")
    print(rock)
    print("\n Paper defeats rock. So you won")

  else:
    print("user choice is:\n")
    print(rock)
    print("computer choice is:\n")
    print(scissors)
    print("\nScissors defeats paper. So you lost")

elif user_choice=='scissors':
  if computer_choice=='rock':
    print("user choice is:\n")
    print(scissors)
    print("computer choice is:\n")
    print(rock)
    print("\n rock defeats scissors. So you lost")

  else:
    print("user choice is:\n")
    print(scissors)
    print("computer choice is:\n")
    print(paper)
    print("\nScissors defeats paper. So you won")

else:
  print("Invalid entry. Please try again.")
