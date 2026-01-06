arr=[]
num=int(input())
for i in range(num):
    arr.append(int(input()))
arr1=set(arr)
length=len(arr1)
print(f"There are {length} distinct element in the array.")
