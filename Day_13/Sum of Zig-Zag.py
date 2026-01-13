# Day 13
# Problem: Sum of Zig-Zag Pattern
# Topic: Python Matrices
# Language: Python

# Input matrix size
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []
zigzag_sum = 0

# Check for square matrix
if n == m:
    # Input matrix
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # Calculate zig-zag sum
    for i in range(n):
        if i == 0 or i == n - 1:
            zigzag_sum += sum(matrix[i])
        else:
            zigzag_sum += matrix[i][n // 2]

    print(f"Sum of Zig-Zag pattern is {zigzag_sum}")
else:
    print("Invalid Input")
