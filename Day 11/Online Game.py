n=int(input())
a=list(map(int,input().split()))
left=0
right=n-1
while left<right:
    while a[left]%2==0:
        left+=1
    while a[right]%2!=0:
        right-=1
    if left<right:
        t=a[left]
        a[left]=a[right]
        a[right]=t
        left+=1
        right-=1
print("Array after Segregation")
for i in range(len(a)):
    print(a[i],end=" ")
