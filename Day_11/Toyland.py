n = int(input())
houses = []
for _ in range(n):
    house_num, pos = map(int,input().split())
    houses.append((house_num,pos))
def get_position(house):
    return house[1]
houses.sort(key=get_position)
max_distance = -1
house1, house2 = -1, -1
for i in range(1, n):
    distance = houses[i][1] - houses[i - 1][1]
    if distance > max_distance:
        max_distance = distance
        housepair = (houses[i - 1][0], houses[i][0])
print(min(housepair),max(housepair))
