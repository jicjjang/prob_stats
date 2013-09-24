from thinkstats import Pmf
from thinkstats import myplot
from matplotlib import pyplot

hist = Pmf.MakeHistFromList([1, 2, 2, 3, 5])
print 'type(hist):', type(hist)
print 'hist.Freq(2):', hist.Freq(2)
print 'hist.Freq(4):', hist.Freq(4)
print 'hist.Values():', hist.Values()
print 'hist.Items():', hist.Items()

myplot.Hist(hist)
pyplot.show()
