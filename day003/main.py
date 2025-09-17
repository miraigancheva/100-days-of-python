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
# Start of the Treasure Island game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision point
# Ask the player whether to go 'left' or 'right'
first_question = input("You're at a cross road. Where do you want to go? - type 'left' or 'right': ")

if first_question == "left":
    # If player chooses left, continue the story at the lake
    print("You've come to a lake. There is an island in the middle of the lake.")

    # Second decision point
    # Ask the player to 'wait' for a boat or 'swim' across
    second_question = input("Type 'wait' to wait for a boat. Type 'swim' to swim across: ")

    if second_question == "wait":
        # If player waits, they reach the island safely
        print("You arrive at the island unharmed. There is a house with 3 doors.")

        # Third decision point
        # Ask the player which door to choose: red, yellow, or blue
        third_question = input("One red, one yellow and one blue. Which colour do you choose? ")

        if third_question == "red":
            # Choosing red means the player loses
            print("It's a room full of fire. Game Over.")
        elif third_question == "yellow":
            # Choosing yellow means the player wins
            print("You found the treasure! You Win!")
        else:
            # Any other choice (blue or invalid input) means the player loses
            print("You enter a room of beasts. Game Over.")
    else:
        # If the player swims instead of waiting, they lose
        print("You get attacked by an angry trout. Game Over.")
else:
    # If the player chooses right at the start, they lose
    print("You fell into a hole. Game Over.")
