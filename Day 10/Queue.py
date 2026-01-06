n,m=map(int,input().split())
group=list(map(int,input().split()))
bus=0
cap=0
for j in group:
    if cap+j<=m:
        cap+=j
    else:
        bus+=1
        cap=j
if cap>0:
    bus+=1
print(bus)
