# Day 11
# Problem: Toyland
# Platform: HackerRank
# Topic: Python Sorting / Tuples
# Language: Python

# Input number of houses
n = int(input("Enter number of houses: "))

# Input house number and position
houses = []
for _ in range(n):
    house_num, pos = map(int, input().split())
    houses.append((house_num, pos))

# Sort houses based on position
houses.sort(key=lambda x: x[1])

max_distance = -1
house_pair = (0, 0)

# Find the maximum distance between adjacent houses
for i in range(1, n):
    distance = houses[i][1] - houses[i - 1][1]
    if distance > max_distance:
        max_distance = distance
        house_pair = (houses[i - 1][0], houses[i][0])

# Print the house numbers in ascending order
print(min(house_pair), max(house_pair))
