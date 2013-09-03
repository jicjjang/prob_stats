import random # include random module
import sys # for sys.argv

def roll_dice(): #function definition
    return random.randint(1,6)

if len(sys.argv) >= 2:
    n_trial = int(sys.argv[1]) # argv[0] is the name of this script
else:
    n_trial=2000

print '# of trials:', n_trial
    
roll_sum_results = [0] * 13 # 
for x in range(n_trial):
    roll_sum_results[roll_dice() + roll_dice()] += 1

print roll_sum_results
print 'Prob. that sum is 8:', roll_sum_results[8] / float(n_trial)
