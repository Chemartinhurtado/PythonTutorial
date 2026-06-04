print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You enter a house. You see a room at your right filled with knifes,"
      " at your left, there is a room with shiny lights and a voice calling tour name")
room = input('Type "left" or "right"')

if room == "left" or "Left":

    print("You arrive to a kitchen. Water is dropping from a freezer")

    Fridge = input('''Type "open" to open the freezer or "wait" to do nothing''')

    if Fridge == "open":
        print("You open the fridge, water covers the whole house and you swim inside the fridge\n"
              "An island appears in front of you\n"
              "you are hungry, but you see 3 fruits in front of you,\nwhich one do you want to eat?")

        fruit = input('''Type"Coconut" to open the Coconut\n'''
        '''type "Strawberry" to eat the strawberry\n'''
        '''type "Banana" to eat the Banana''')
        if fruit == "Strawberry":
            print("You die because strawberries are disgusting")
        elif fruit == "Banana":
            print("You Win!")
        elif fruit == "Coconut":
            print("Coconut is too heavy, you die because of yes")
        else:
            print("Game over")

    else:
        print("Someone stabs you from the back, you die")

else:
    print("Suddenly you see all black, someone struck at you from the back and you die")
