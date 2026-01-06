# Day 5
# Problem: Treasure Hunter
# Platform: HackerRank
# Topic: Python Basics / Arithmetic
# Language: Python

# Input values
total = int(input())     # Total treasure value
ben = int(input())       # Ben's percentage
black = int(input())     # Black's percentage

# Calculate Ben's share
ben_share = int(total * (ben / 100))
remaining_after_ben = total - ben_share

# Calculate Black's share from remaining amount
black_share = int(remaining_after_ben * (black / 100))
remaining_after_black = total - (ben_share + black_share)

# Remaining treasure divided equally among 3
each_share = remaining_after_black / 3

# Output
print(ben_share)
print(black_share)
print(int(each_share))
