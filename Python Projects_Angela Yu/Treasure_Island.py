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
print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nAnswer the following questions to find the treasure")

ROUND1= input('You are at a crossroad. Which direction would you like to turn?'
              'Type "Left" or "Right".').lower()
if ROUND1 == "left":
    print("Welcome to the next round!")
    ROUND2 = input('You see an island in the middle of a lake.'
                   'Do you wish to wait or a boat or swim through the lake to reach the island?'
                   'Type "wait" or "swim".').lower()
    if ROUND2=="wait":
        print("Welcome to the next round!")
        ROUND3= input('The treasure is behind a door. There is a house with 3 doors in different colors.'
                      'Which door will you choose?'
                      'Type "Red" or "Blue" or "Yellow".').lower()
        if ROUND3== "yellow":
            print("Congratulations!! You have won the treasure.")
        elif ROUND3 == "red":
            print("You got caught in the fire---GAME OVER--BETTER LUCK NEXT TIME!")
        elif ROUND3== "blue":
            print("You entered the room of beasts---FGAME OVER---BETTER LUCK NEXT TIME!")
        else:
            print("You choose a door that does not exist---GAME OVER!")
    else:
        print("A crocodile just ate you---GAME OVER!")
else:
    print("You fell into a hole---GAME OVER!")