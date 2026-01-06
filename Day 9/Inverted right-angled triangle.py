# Day 9
# Problem: Inverted Right-Angled Triangle
# Platform: HackerRank
# Topic: Python Loops / Patterns
# Language: Python

# Input the number of rows
num = int(input("Enter the number of rows: "))

# Loop from num down to 1
while num >= 1:
    # Print stars in each row
    for i in range(num):
        print("*", end="")
    print()  # Move to next line
    num -= 1
