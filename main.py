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
print("Your mission is to find the treasure.") 
print("You are escaping from a giant monster and suddenly the path divides into two.")

choice1 = input("Which path do you take: left or right? ")

if choice1 == 'right':
  print("Oh no! You have made a terrible mistake.\n The right path has lead you to a deadly cliff.\n GAME OVER :(")

elif choice1 == 'left':
  print("Great! You avoided a deadly cliff.\n Your journey continues...")

  print("As you move on, you have found yourself in a difficult situation.\n In order to continue your journey you must cross a whitewater river.\n Fortunately, since it's next to a tourist location it is likelty that someone may pass by soon.\n However, this is uncertain and perhaps the best choice is to swim across it.")

  choice2 = input("What do you do: swim or wait? ")

  if choice2 == 'swim':
    print("Damn, this is bad.\n Since you decided to swim across the river a shoal of hungry trout has started to attack you.\n Even through they cause almost no harm to you, it seems impossible for you to cross the river any time soon. \n GAME OVER :(")
  elif choice2 == 'wait':
    print("Waiting rewards the brave.\n Congratulations! Lucky for you, a couple of fisherman helped you out in this unfortunate situation.\n You have thank them and arrived safe and sound to mainland.\n Now you are following the treasure map your great granpa lend you before he passed away.")

    print("You have now reached an imponent building which acording to your map, keeps the treasue chest.\n As you get into it, you face three doors, yet it isn't marked in your map which one should you take.\n The sound of intruders is getting louder and louder.")

    choice3 = input("You must decide, which door will you take: red, yellow or blue? ")

    if choice3 == 'red':
      print("Oh my god! Now I see why the door was red... the room inside it's on fire.\n But.. you locked the door! This is a complete disaster.\n I guess you'll join your great grandpa in the afterlife soon.\n GAME OVER :(")
    elif choice3 == 'yellow':
      print("Of course! The golden color has lead you to the treasue chest.\n It seems you are wealthy now.\n Yet, great power comes with great responsability, so spend your treasue wisely.\n YOU HAVE WON!!! :D")
    elif choice3 == 'blue':
      print("Poor you! Due to the hurry you didn't read that the blue door lead to the bear's captivity... and they are quite hungry!\n I wonder how you will escape.\n GAME OVER :(")