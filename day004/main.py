import random

# ASCII art for Rock, Paper, and Scissors
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

# Store all options in a list for easy access
game_images = [rock, paper, scissors]

# Ask the user for their choice (0 = Rock, 1 = Paper, 2 = Scissors)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Check if the user entered a valid number
if user_choice >= 0 and user_choice <= 2:
    # Print the corresponding ASCII art for the user's choice
    print(game_images[user_choice])

# Randomly select the computer's choice (0, 1, or 2)
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Determine the winner
if user_choice >= 3 or user_choice < 0:
    # Handle invalid inputs (anything other than 0, 1, 2)
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    # Rock beats Scissors
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    # Rock beats Scissors (reverse case)
    print("You lose!")
elif computer_choice > user_choice:
    # Higher number wins (Paper beats Rock, Scissors beats Paper)
    print("You lose!")
elif user_choice > computer_choice:
    # Reverse of above
    print("You win!")
elif computer_choice == user_choice:
    # Same choice means a draw
    print("It's a draw!")
