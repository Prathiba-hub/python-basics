# Day 8
# Problem: Hollow Square Pattern
# Platform: HackerRank
# Topic: Python Loops / Patterns
# Language: Python

# Input the size of the square
num = int(input("Enter the size of the square: "))

# Loop through each row
for row in range(num):
    # Loop through each column
    for col in range(num):
        # Print '*' for borders, space for inner area
        if row == 0 or row == num - 1 or col == 0 or col == num - 1:
            print("*", end="")
        else:
            print(" ", end="")
    # Move to next line after each row
    print()
