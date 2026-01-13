def cal_sum(o_arr):
    if len(o_arr)==0:
        return 0
    else:
        return o_arr[0]+cal_sum(o_arr[1:])
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
odd_arr=[]
for i in arr:
    if i%2!=0 and i>0:
        odd_arr.append(i)
s=cal_sum(odd_arr)
print(f"Sum = {s}")
