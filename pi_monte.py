import random

incircle = 0
total = 10000

for i in range(total):
    x = random.random()
    y = random.random()

    if x * x + y * y < 1:
        incircle += 1

print 4 * float(incircle) / total
