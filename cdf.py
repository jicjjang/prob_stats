from thinkstats import Cdf
from thinkstats import myplot

t = [2, 1, 3, 2, 5]
cdf = Cdf.MakeCdfFromList(t)
cdf.name = 'Sample'

print 'cdf.Prob(2):', cdf.Prob(2)
print 'cdf.Prob(3):', cdf.Prob(3)
print 'cdf.Prob(6):', cdf.Prob(6)

print 'cdf.Value(0.5):', cdf.Value(0.5)
print 'cdf.Value(0.7):', cdf.Value(0.7)

myplot.Clf()
myplot.Cdf(cdf)
myplot.Show(title='CDF', xlabel='x', ylabel='CDF(x)', axis=[0, 6, 0, 1])
