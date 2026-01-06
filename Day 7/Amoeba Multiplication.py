# Day 7
# Problem: Amoeba Multiplication
# Platform: HackerRank
# Topic: Python Loops / Arithmetic
# Language: Python

# Input number of amoebas
amoebas = int(input())

# Initialize population
population = 1

# Multiply amoebas every hour for the given number
for _ in range(amoebas):
    population *= 2

# Print the final population
print(population)
