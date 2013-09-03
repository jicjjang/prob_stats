import random # include random module
import sys # for sys.argv

def roll_dice(): #function definition
    return random.randint(1,6)

if len(sys.argv) >= 2:
    n_trial = int(sys.argv[1]) # argv[0] is the name of this script
else:
    n_trial=2000

print '# of trials:', n_trial
    
roll_results = []#

for x in range(n_trial):
    roll_results.append([roll_dice(), roll_dice()])

roll_results_has_two = [xx for xx in roll_results if 2 in xx]

roll_results_has_two_sum8 = [xx8 for xx8 in roll_results_has_two if sum(xx8) == 8]

#print roll_results_has_two
#print roll_results_has_two_sum8
prob = len(roll_results_has_two_sum8) / float(len(roll_results_has_two))
print 'Prob. that sum is 8 when one is 2:', prob
