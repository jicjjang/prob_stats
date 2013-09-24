from thinkstats import Pmf
from thinkstats import myplot
from matplotlib import pyplot

pmf = Pmf.MakePmfFromList([1, 2, 2, 3, 5])
print 'type(pmf):', type(pmf)
print 'pmf.Prob(2):', pmf.Prob(2)
print 'pmf.Incr(2, 0.2)'
pmf.Incr(2, 0.2)
print 'pmf.Prob(2):', pmf.Prob(2)
print 'pmf.Mult(2, 0.5)'
pmf.Mult(2, 0.5)
print 'pmf.Prob(2):', pmf.Prob(2)

print 'pmf.Total():', pmf.Total()

print 'pmf.Normalize()'
pmf.Normalize()
print 'pmf.Total():', pmf.Total()

myplot.Hist(pmf)
pyplot.show()
