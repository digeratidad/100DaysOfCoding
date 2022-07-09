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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Shicktopia Island")
print("Your mission is to find the treasure")

direction = input('You are at a crossroad, which direction do you want to go? Enter "left" or "right"\n').lower()

if not direction == "left":
    print("You have fallen in a hole and are dead. Game Over!")

if direction == "left":
    swim = input('You have arrived at a lake. Would you like to do "swim" or "wait"?\n').lower()
    if not swim == "wait":
        print("You were attacked by a trout. Game Over!")

    if swim == "wait":
        door = input('You were picked up by a boat and made it across the lake. You see a house with three doors, one is'
                     ' "red", one is "yellow", and one is "blue". Which door do you choose?\n').lower()

        if door == "red":
            print("You were burned by fire. Game Over!")
        elif door =="yellow":
            print("You found the treasure. You Win!")
        elif door == "blue":
            print("You were eaten by beasts. Game Over!")
        else:
            print("Game Over!")
