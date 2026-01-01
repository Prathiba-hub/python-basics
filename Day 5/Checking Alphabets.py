c = input()
vowel = ['a', 'e', 'i', 'o', 'u']

if c.isalpha():
    if c.lower() in vowel:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
