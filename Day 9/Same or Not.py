arr1=[]
val1=int(input())
val2=int(input())
for i in range(val1):
    ans=int(input())
    arr1.append(ans)
arr2=[]
for i in range(val2):
    ans1=int(input())
    arr2.append(ans1)
add1=sum(arr1)
add2=sum(arr2)
length1=len(arr1)
length2=len(arr2)
if add1==add2 and length1==length2:
    print("Same")
else:
    print("Not Same")
