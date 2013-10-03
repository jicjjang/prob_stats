from thinkstats import Cdf
from thinkstats import myplot

word_count = {}

fp = open('thinkstats.txt', 'rt')
text = fp.read()
words = text.split()
print len(words)
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

cdf = Cdf.MakeCdfFromList(word_count.values())
print 'Median:', cdf.Value(0.5)
print 'Mean:', cdf.Mean()
print 'Mode:', cdf.Value(1.0)

myplot.Clf()
myplot.Cdf(cdf, complement=True)
myplot.Show(xscale='log', yscale='log')
    

