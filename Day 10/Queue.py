# Day 10
# Problem: Queue / Bus Capacity
# Platform: HackerRank
# Topic: Python Lists / Greedy Algorithm
# Language: Python

# Input number of groups and bus capacity
n, m = map(int, input("Enter number of groups and bus capacity: ").split())

# Input group sizes
group = list(map(int, input("Enter the group sizes: ").split()))

bus_count = 0  # Number of buses used
current_capacity = 0  # Current bus capacity used

# Allocate groups to buses
for people in group:
    if current_capacity + people <= m:
        current_capacity += people  # Add group to current bus
    else:
        bus_count += 1  # Current bus full, use new bus
        current_capacity = people

# Count the last bus if it has people
if current_capacity > 0:
    bus_count += 1

# Print total buses needed
print(bus_count)
