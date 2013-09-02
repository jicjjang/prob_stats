import random # include random module

def roll_dice(): #function definition
    return random.randint(1,6)

roll_result = [0] * 6 # roll_result = [0, 0, 0, 0, 0, 0]
for x in range(20):
    roll_result[roll_dice() - 1] += 1

print roll_result
