# Day 6
# Problem: Trendy Number
# Platform: HackerRank
# Topic: Python Conditional Statements
# Language: Python

# Input a three-digit number
val = int(input())

# Check if the number is three digits
if 100 <= val <= 999:
    # Extract the tens digit
    tens_digit = (val // 10) % 10
    
    # Check if tens digit is divisible by 3
    if tens_digit % 3 == 0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
else:
    print("Invalid Number")
