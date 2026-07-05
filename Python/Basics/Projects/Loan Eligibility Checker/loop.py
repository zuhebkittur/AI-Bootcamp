# The program should:

# Ask the user to enter a number.
# Use a for loop.
# Print the multiplication table from 1 to 10.

number = int(input("Enter the Number: "))

for i in range(1, 11):
   multily = multiplication = number * i
   print(f"{number} * {i} =", multily)