# Day 13
# Problem: Magic Square
# Topic: Python Matrices
# Language: Python

n = int(input())
matrix = []

# Reading the square matrix
for _ in range(n):
    matrix.append(list(map(int, input().split())))

zigzag_sum = 0

for i in range(n):
    if i == 0 or i == n - 1:
        zigzag_sum += sum(matrix[i])   # First and last row
    else:
        zigzag_sum += matrix[i][1]     # Middle element of other rows

print(f"Sum of Zig-Zag pattern is {zigzag_sum}")
