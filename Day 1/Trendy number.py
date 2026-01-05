# Day 1
# Problem: Trendy Number
# Platform: HackerRank
# Topic: Conditional Statements
# Language: Python

val = int(input())

if 100 <= val <= 999:
    middle_digit = (val // 10) % 10
    if middle_digit % 3 == 0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
else:
    print("Invalid Number")
