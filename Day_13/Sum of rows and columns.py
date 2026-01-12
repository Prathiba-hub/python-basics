rows = int(input().strip())
cols = int(input().strip())
matrix = []
for _ in range(rows):
    row = list(map(int, input().strip().split()))
    matrix.append(row)
row_sums = []
for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
col_sums = []
for j in range(cols):
    col_sum = sum(matrix[i][j] for i in range(rows))
    col_sums.append(col_sum)
max_row_sum = max(row_sums)
max_row_index = row_sums.index(max_row_sum) + 1 
max_col_sum = max(col_sums)
max_col_index = col_sums.index(max_col_sum) + 1  
print(f"The Sum of rows is {' '.join(map(str, row_sums))}")
print(f"Row {max_row_index} has a maximum sum")
print(f"The Sum of columns is {' '.join(map(str, col_sums))}")
print(f"Column {max_col_index} has the maximum sum")
    
