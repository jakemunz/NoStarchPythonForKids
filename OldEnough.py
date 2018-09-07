# OldEnough.py Using boolean conditional expressions
driving_age = eval(input("What is the legal driving age where you live? ")) # Here we evaluate the number the user inputs
your_age = eval(input("How old are you? "))     # Here we evealuate the number the user inputs
if your_age >= driving_age:     # Checks the users age is greater than or equal to the driving age
    print("You're old enough to drive!")
if your_age < driving_age:      # Checks the users age is less than the driving_age
    print("Sorry, you can drive in", driving_age - your_age, "years.")      # Tell s the user how many years until they can drive by subtracting the users age from the driving age
