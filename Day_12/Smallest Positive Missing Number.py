n=int(input())
arr=list(map(int,input().split()))
positive_numbers = [num for num in arr if num > 0]
positive_numbers.sort()

smallest_missing = 1  
for num in positive_numbers:
    if num == smallest_missing:
        smallest_missing += 1  
print(smallest_missing)
