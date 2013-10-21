from thinkstats import Cdf
from thinkstats import myplot
import random

def paretovariate(alpha, Xm = 1.0):
    return random.paretovariate(alpha) * Xm

samples = [paretovariate(1.7, 100.0) for x in range(1000000)]

cdf = Cdf.MakeCdfFromList(samples)
print 'Median:', cdf.Value(0.5), ' cm'
print 'Mean:', cdf.Mean(), ' cm'
print 'Tallest:', cdf.Value(1.0), ' cm'



