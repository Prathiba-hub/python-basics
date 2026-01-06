# Day 10
# Problem: Compatible Array
# Platform: HackerRank
# Topic: Python Lists / Conditional Checks
# Language: Python

# Input first array
arr1 = []
num1 = int(input("Enter number of elements in first array: "))
for _ in range(num1):
    arr1.append(int(input()))

# Input second array
arr2 = []
num2 = int(input("Enter number of elements in second array: "))
for _ in range(num2):
    arr2.append(int(input()))

# Check compatibility
compatible = True
if num1 != num2:
    compatible = False
else:
    for i, j in zip(arr1, arr2):
        if i < j:
            compatible = False
            break

# Print result
if compatible:
    print("Compatible")
else:
    print("Incompatible")
