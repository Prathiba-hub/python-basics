def count_num(n):
    if n<10:
        return 1
    else:
        return 1 + count_num(n//10)
num = int(input())
dig = count_num(num)
print(f"The number of digits in {num} is {dig}")
