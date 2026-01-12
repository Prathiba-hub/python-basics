num=int(input())
arr=[]
for i in range(num):
    arr.append(input().strip())
for j in arr:
    sorted_string = ''.join(sorted(j, reverse=True))
    print(sorted_string)
    
