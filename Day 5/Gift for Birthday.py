# Day 5
# Problem: Leap Year Check
# Platform: HackerRank
# Topic: Python Conditional Statements
# Language: Python

# Input a year
year = int(input())

# Check for leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
