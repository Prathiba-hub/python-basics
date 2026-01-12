num=int(input())
num2=num*num
arr=[]
for i in range(num):
    arr.append(list(map(int,input().split())))
count1=0
count2=0
for i in range(num):
    for j in range(num):
        if arr[i][j]%2==0:
            count1+=1
        else:
            count2+=1
if num2==count1 or num2==count2:
    print("Yes")
else:
    print("No")

