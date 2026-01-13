# Day 13
# Problem: Sum of Rows and Columns
# Topic: Python Matrices
# Language: Python

rows = int(input())
cols = int(input())

matrix = []

# Reading the matrix
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

# Sum of each row
row_sums = []
for i in range(rows):
    row_sums.append(sum(matrix[i]))

# Sum of each column
col_sums = []
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    col_sums.append(col_sum)

# Finding maximum row sum and column sum
max_row_sum = max(row_sums)
max_row_index = row_sums.index(max_row_sum) + 1

max_col_sum = max(col_sums)
max_col_index = col_sums.index(max_col_sum) + 1

# Output
print(f"The Sum of rows is {' '.join(map(str, row_sums))}")
print(f"Row {max_row_index} has a maximum sum")
print(f"The Sum of columns is {' '.join(map(str, col_sums))}")
print(f"Column {max_col_index} has the maximum sum")
