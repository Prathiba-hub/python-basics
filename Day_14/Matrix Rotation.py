num=int(input())
arr=[]
for i in range(num):
    arr.append(list(map(int,input().split())))
for i in range(num):
    for j in range(num-1,-1,-1):
        print(arr[j][i],end=" ")
    print()
