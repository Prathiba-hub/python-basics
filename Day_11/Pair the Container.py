# Day 11
# Problem: Pair the Container
# Platform: HackerRank
# Topic: Python Arrays / Two Pointer Technique
# Language: Python

# Input number of containers
N = int(input("Enter number of containers: "))

# Input container capacities
capacities = list(map(int, input("Enter the capacities: ").split()))

# Sort capacities
capacities.sort()

left = 0
right = N - 1
pairs = []

# Pair largest with smallest
while left < right:
    pairs.append((capacities[right], capacities[left]))
    left += 1
    right -= 1

# If one container remains unpaired
if left == right:
    pairs.append((capacities[left], 0))

# Output result
for pair in pairs:
    print(pair[0], pair[1])
