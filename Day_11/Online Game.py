# Day 11
# Problem: Online game
# Platform: HackerRank
# Topic: Python Arrays / Two Pointers
# Language: Python

# Input size of array
n = int(input("Enter number of elements: "))

# Input array elements
a = list(map(int, input("Enter the elements: ").split()))

left = 0
right = n - 1

# Two-pointer approach to segregate even and odd numbers
while left < right:
    while left < right and a[left] % 2 == 0:
        left += 1
    while left < right and a[right] % 2 != 0:
        right -= 1

    if left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

# Output
print("Array after Segregation")
for element in a:
    print(element, end=" ")
