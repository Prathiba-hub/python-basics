N=int(input())
capacities=list(map(int,input().strip().split()))
capacities.sort()
pairs=[]
left=0
right=N-1
while left<right:
    pairs.append((capacities[right],capacities[left]))
    left+=1
    right-=1
if left==right:
    pairs.append((capacities[left],0))
for pair in pairs:
    print(pair[0],pair[1])

    
