num=int(input())
num2=num
arr=[]
for i in range(num):
    arr.append(list(map(int,input().split())))
add1=0
add2=0
for i in range(num):
    ans=arr[i]
    add1+=ans[i]
for i in range(num):
    ans1=arr[i]
    add2+=ans1[num2-1]
    num2-=1
if add1==add2:
    print("Yes")
else:
    print("No")
        
        
