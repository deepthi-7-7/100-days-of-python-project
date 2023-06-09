print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 


option1=input("Select which way you wanted to go (Left/Right)? \n").lower()
if option1=='left':
  print("Now you have reached to the river. You wanna swim or wait?\n")
  option2=input("Type 'swim' to swim across the river or type 'wait' to wait near the shore.\n").lower()
  if option2=='wait':
    print("Wow you've waited so you got the chance to select the door.\n")
    option3=input("Choose which door you wanted to open (red,blue,yellow)\n").lower()
    if option3=='yellow':
      print("Hurray! you've finally found the treasure.")
    else:
      print("Oops you chose wrong door. You've lost the game")
  else:
    print("Oops you chose wrong option. You've lost the game")

else:
  print("Oops you chose wrong path. You've lost the game")
