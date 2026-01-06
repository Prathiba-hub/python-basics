# Day 9
# Problem: Trapezium Pattern
# Platform: HackerRank
# Topic: Python Loops / Patterns
# Language: Python

# Input the number of rows
n = int(input("Enter the number of rows: "))

# Initialize left and right halves
left_half = 1
right_half = n ** 2 + 1

# Loop through rows from top to bottom
for i in range(n, 0, -1):
    # Print leading dashes for trapezium shape
    for j in range(n, i, -1):
        print("--", end="")

    # Print left half numbers
    for k in range(1, i + 1):
        print(left_half, end="*")
        left_half += 1

    # Print right half numbers
    for l in range(1, i + 1):
        print(right_half, end="")
        if l < i:
            print("*", end="")
        right_half += 1

    # Move to next line
    print()

    # Adjust right_half for next row
    right_half = right_half - (i - 1) * 2 - 1
