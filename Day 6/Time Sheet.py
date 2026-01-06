# Day 6
# Problem: Time Sheet / Weekly Salary Calculation
# Platform: HackerRank
# Topic: Python Arithmetic & Conditional Statements
# Language: Python

# Input hours worked each day (day1 = Sunday, day2 = Monday, ..., day7 = Saturday)
day1 = int(input())
day2 = int(input())
day3 = int(input())
day4 = int(input())
day5 = int(input())
day6 = int(input())
day7 = int(input())

# Calculate total hours from Monday to Friday
weekday_hours = day2 + day3 + day4 + day5 + day6

# Base salary: Rs.100 per weekday hour
salary = weekday_hours * 100

# Add overtime for weekdays (hours > 8)
for d in [day2, day3, day4, day5, day6]:
    if d > 8:
        salary += (d - 8) * 15

# Add weekly overtime if total weekday hours > 40
if weekday_hours > 40:
    salary += (weekday_hours - 40) * 25

# Add weekend pay with bonus
# Saturday (day7) 25% bonus
if day7 > 0:
    bonus_sat = int(day7 * 0.25 * 100)
    salary += day7 * 100 + bonus_sat

# Sunday (day1) 50% bonus
if day1 > 0:
    bonus_sun = int(day1 * 0.50 * 100)
    salary += day1 * 100 + bonus_sun

# Print total salary
print(salary)
