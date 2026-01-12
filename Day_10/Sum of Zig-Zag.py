num1=int(input())
num2=int(input())
arr=[]
add=0
if num1==num2:
    for i in range(num1):
        l=list(map(int,input().split()))
        arr.append(l)
    for i in range(num1):
        if i==0 or i==num1-1:
            add+=sum(arr[i])
        else:
            ans=arr[i]
            add+=ans[1]
                
                
print(f"Sum of Zig-Zag pattern is {add}")
        
