from thinkstats import Cdf
from thinkstats import myplot
import random

def paretovariate(alpha, Xm = 1.0):
    return random.paretovariate(alpha) * Xm

samples = [paretovariate(1.0, 1.0) for x in range(80)]

cdf = Cdf.MakeCdfFromList(samples)
myplot.Clf()
myplot.Cdf(cdf, complement=True)
myplot.Show(xscale='log', yscale='log')

