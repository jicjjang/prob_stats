import thinkstats.thinkstats as ts
import math

pumpkins = [200, 250, 500, 550, 2000, 2500]
print 'Mean of pumpkins:', ts.Mean(pumpkins), 'g'
print 'Variance of pumpkins:', ts.Var(pumpkins), 'g^2'
print 'Standard Dev. of pumpkins:', math.sqrt(ts.Var(pumpkins)), 'g'
