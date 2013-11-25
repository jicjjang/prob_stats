import randvar
from thinkstats import Cdf
from math import log
from math import exp
from thinkstats import correlation

exponential = randvar.Exponential(0.6)

sample = [exponential.generate() for _ in range(1000)]
cdf = Cdf.MakeCdfFromList(sample)

xs = []
ys = []
for x, y in cdf.Items():
    if y == 1.0:
        continue
    xs.append(x)
    ys.append(-log(1.0-y))

inter, slope = correlation.LeastSquares(xs, ys)

lam = slope

print 'lambda', lam
