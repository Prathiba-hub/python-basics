# Day 6
# Problem: Scholarship Eligibility
# Platform: HackerRank
# Topic: Python Conditional Statements
# Language: Python

# Input student details
age = int(input())
year = int(input())
income = int(input())
arrear = int(input())
marks = float(input())
attendance = float(input())

# Check eligibility
if year >= 2021 and 18 <= age <= 21 and arrear <= 2 and income <= 200000 and marks >= 60 and attendance >= 80:
    print("Eligible")
elif year >= 2021 and 18 <= age <= 21 and 2 < arrear and 200000 <= income <= 250000 and marks >= 80 and attendance >= 90:
    print("Partially Eligible")
else:
    print("Not Eligible")
