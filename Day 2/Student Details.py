# Day 2
# Problem: Student Details
# Platform: HackerRank
# Topic: Python Basics
# Language: Python

name = input()
age = int(input())
cgpa = float(input())
grade = input()

# Truncate CGPA to 2 decimal places
cgpa_truncated = int(cgpa * 100) / 100

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa_truncated)
print("Grade:", grade)
