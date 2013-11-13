from thinkstats import Cdf
from thinkstats import cumulative
from thinkstats import myplot
from thinkstats import thinkstats
import matplotlib.pyplot as pyplot
import math
import random

   
def PValue(model1, model2, n, m, delta, iters=1000):
    deltas = [Resample(model1, model2, n, m) for i in range(iters)]
    cdf = Cdf.MakeCdfFromList(deltas)

    # compute the two tail probabilities
    left = cdf.Prob(-delta)
    right = 1.0 - cdf.Prob(delta)
    
    pvalue = left + right

    return cdf, pvalue


def PlotCdf(root, cdf, delta):
    """Draws a Cdf with vertical lines at the observed delta.

    Args:
       root: string used to generate filenames
       cdf: Cdf object
       delta: float observed difference in means    
    """
    def VertLine(x):
        """Draws a vertical line at x."""
        xs = [x, x]
        ys = [0, 1]
        pyplot.plot(xs, ys, linewidth=2, color='0.7')
        
    VertLine(-delta)
    VertLine(delta)

    xs, ys = cdf.Render()    
    pyplot.subplots_adjust(bottom=0.11)
    pyplot.plot(xs, ys, linewidth=2, color='blue')
    
    myplot.Save(root,
                title='Resampled differences',
                xlabel='difference in means',
                ylabel='CDF(x)',
                legend=False)

    myplot.Close()
    

def Resample(t1, t2, n, m):
    sample1 = [random.choice(t1) for i in range(n)]
    sample2 = [random.choice(t2) for i in range(m)]
    delta = thinkstats.Mean(sample1) - thinkstats.Mean(sample2)
    return delta
 
if __name__ == "__main__":
    # get the data
    pool, firsts, others = cumulative.MakeTables('thinkstats')
    mean_var = thinkstats.MeanVar(pool.lengths)
    
    n = len(firsts.lengths)
    m = len(others.lengths)

    print 'Gestation:'
    mu1, mu2 = thinkstats.Mean(firsts.lengths), thinkstats.Mean(others.lengths)
    delta = abs(mu1 - mu2)
    # observed delta

    cdf, pvalue = PValue(pool.lengths, pool.lengths, n, m, delta)
    print 'n:', n
    print 'm:', m
    print 'mu1', mu1
    print 'mu2', mu2
    print 'delta', delta
    print 'p-value', pvalue

    PlotCdf('resampled_diff_gest', cdf, delta)

    print 'Weights:'
    mu1, mu2 = thinkstats.Mean(firsts.weights), thinkstats.Mean(others.weights)
    delta = abs(mu1 - mu2)
    # observed delta

    cdf, pvalue = PValue(pool.weights, pool.weights, n, m, delta)
    print 'n:', n
    print 'm:', m
    print 'mu1', mu1
    print 'mu2', mu2
    print 'delta', delta
    print 'p-value', pvalue

    PlotCdf('resampled_diff_weight', cdf, delta)

