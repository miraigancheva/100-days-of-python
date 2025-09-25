print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $")) # bill input
tip = int(input("What percentage tip would you like to give? 10 12 15 ")) # tip input
people = int(input("How many people to split the bill? ")) # people input
person_pay = round(((bill / people) * (tip / 100 + 1)), 2) # calculate how much each person should pay
print(f"Each person should pay: ${person_pay:.2f}") # print result

