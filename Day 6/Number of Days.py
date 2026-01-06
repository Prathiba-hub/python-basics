# Day 6
# Problem: Number of Days
# Platform: HackerRank
# Topic: Python Conditional Statements / Leap Year
# Language: Python

# Input year and month
year = int(input())
month = int(input())

# Lists of months with 31 and 30 days
months_31 = [1, 3, 5, 7, 8, 10, 12]
months_30 = [4, 6, 9, 11]

# Check for valid year and month
if 1900 <= year <= 9999 and 1 <= month <= 12:
    if month in months_31:
        print("31 Days")
    elif month in months_30:
        print("30 Days")
    else:  # February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("29 Days")
        else:
            print("28 Days")
else:
    print("0")  # Invalid input
