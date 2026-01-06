# Day 7
# Problem: Cricket Match Analysis
# Platform: HackerRank
# Topic: Python Arithmetic / Conditional Statements
# Language: Python

# Input total balls in match, total runs, current score, and balls played
total_balls = int(input())
total_runs = int(input())
score_runs = int(input())
balls_played = int(input())

# Calculate total overs in the match
total_overs = total_balls // 6

# Calculate overs completed (as decimal)
overs_whole = balls_played // 6
overs_remaining_balls = balls_played % 6
overs_finished = overs_whole + overs_remaining_balls / 10

# Calculate current run rate (CRR) and target run rate (TRR)
crr = score_runs / overs_finished
trr = total_runs / total_overs

# Print overs and run rates
print(total_overs)
print(f"{overs_finished:.1f}")
print(f"{crr:.1f}")
print(f"{trr:.1f}")

# Determine if eligible to win
if crr > trr:
    print("Eligible to Win")
else:
    print("Not Eligible to Win")
