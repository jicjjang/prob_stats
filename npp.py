from thinkstats import rankit
from thinkstats import myplot
import random

sample = [random.normalvariate(0.0, 1.0) for i in range(100)]

means = rankit.EstimateRankits(len(sample))
myplot.Plot(means, sorted(sample), 'b.', markersize=3)
myplot.Save('rankit_npp', xlabel='rankits')

rankit.MakeNormalPlot(sample, 'dirty_npp')

myplot.Close()
