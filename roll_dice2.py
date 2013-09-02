import random # include random module

def roll_dice(): #function definition
    return random.randint(1,6)

n_trial=2000
roll_sum_results = [0] * 13 # 
for x in range(n_trial):
    roll_sum_results[roll_dice() + roll_dice()] += 1

print roll_sum_results
print roll_sum_results[8] / float(n_trial)
