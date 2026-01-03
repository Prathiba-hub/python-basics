import math
t_ball=int(input())
t_runs=int(input())
score_runs=int(input())
n_balls=int(input())
t_overs=t_ball//6
over_whole=n_balls//6
over_half=n_balls%6
overs_finished=over_whole+(over_half)/10
crr=score_runs/overs_finished
trr=t_runs/t_overs
print(f"{t_overs}")
print(f"{overs_finished}")
print(f"{crr:.1f}")
print(f"{trr:.1f}")
if crr>trr:
    print("Eligible to Win")
else:
    print("Not Eligible to Win")
