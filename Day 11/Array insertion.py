arr=[]
num=int(input())
for i in range(num):
    arr.append(int(input()))
pos=int(input())
if pos<=len(arr):
    val=int(input())
    arr.insert(pos-1,val)
    print("Array after insertion is")
    for i in arr:
        print(i)
else:
    print("Invalid Input")
