from thinkstats import Cdf
from thinkstats import myplot
import random

samples = [random.expovariate(2) for x in range(80)]

cdf = Cdf.MakeCdfFromList(samples)
myplot.Clf()
myplot.Cdf(cdf, complement=True)
myplot.Show(yscale='log')

