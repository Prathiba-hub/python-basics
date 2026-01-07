arr=[]
num=int(input())
for i in range(num):
    arr.append(int(input()))
unique_arr = []
seen = set()

for item in arr:
    if item not in seen:
        seen.add(item)
        unique_arr.append(item)

for i in unique_arr:
    print(i)
