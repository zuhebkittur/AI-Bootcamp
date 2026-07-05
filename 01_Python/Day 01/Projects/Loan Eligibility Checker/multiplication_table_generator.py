# The program should:

# Ask the user to enter a number.
# Use a for loop.
# Print the multiplication table from 1 to 10.

# number = int(input("Enter the Number: "))

# for i in range(1, 11):
#    multily = multiplication = number * i
#    print(f"{number} * {i} =", multily)

# 5 * 10 = 50
# 5 * 9 = 45
# 5 * 8 = 40
# ...
# 5 * 1 = 5

number = int(input("Enter the Number: "))
for i in range (10, 0, -1):
   multiply = number * i
   print(f"{number} * {i} =", multiply)