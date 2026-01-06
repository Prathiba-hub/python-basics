arr1=[]
num1=int(input())
c=False
for i in range(num1):
    arr1.append(int(input()))
arr2=[]
num2=int(input())
for i in range(num2):
    arr2.append(int(input()))
for i in arr1:
    for j in arr2:
        if i>=j:
            c=True
        else:
            c=False
if c and num1==num2:
    print("Compatible")
else:
    print("Incompatible")
    
