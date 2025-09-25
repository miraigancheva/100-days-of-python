import random

# List of possible characters
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Get user input for how many of each type of character
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Build the password as a list of characters
password_list = []

# Add random letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Add random symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Shuffle the list so the characters are in random order
random.shuffle(password_list)

# Join the list into a single string
password = "".join(password_list)

# Print the final secure password
print(f"Your password: {password}")
