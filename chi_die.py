import random
from thinkstats import chi

def ChiSquared(expected, observed):
    it = zip(expected, observed)
    t = [(obs - exp)**2 / exp for exp, obs in it]
    return sum(t)

def Simulate(n = 60):
    dice_results = [0.0] * 6
    for _ in range(n):
        dice_results[random.randrange(0, 6)] += 1

    return dice_results

if __name__=='__main__':
    num_trials = 1000
    observed = [8.0, 9.0, 19.0, 6.0, 8.0, 10.0]
    expected = [10.0] * 6

    chi_squared = ChiSquared(expected, observed)
    print 'chi-squared statistic', chi_squared

    count = 0
    for _ in range(num_trials):
        simulated = Simulate()
        chi_ = ChiSquared(expected, simulated)
        if chi_ >= chi_squared:
            count += 1

    print 'p-value', count / float(num_trials)

