# Day 5
# Problem: Checking Alphabets
# Platform: HackerRank
# Topic: Python Conditional Statements
# Language: Python

c = input()

vowels = ['a', 'e', 'i', 'o', 'u']

if c.isalpha():
    if c.lower() in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
