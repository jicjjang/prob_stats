import random
import math
import thinkstats.thinkstats as ts
from thinkstats import Cdf
from thinkstats import myplot

def poincare_bread(n=4, nsamples=365):
    poincare = [max([random.normalvariate(950, 50) for x in range(n)]) for y in range(nsamples)]
    mu, var = ts.MeanVar(poincare)
    sd = math.sqrt(var)

    cdf = Cdf.MakeCdfFromList(poincare)
    cdf.name = 'poincare'

    return cdf, mu, sd

if __name__=='__main__':
    nsamples = 365
    cdf_p, mu, sd = poincare_bread(4, nsamples)
    print mu, sd
    
    normal = [random.normalvariate(mu, sd) for y in range(nsamples)]
    cdf_n = Cdf.MakeCdfFromList(normal)
    cdf_n.name = 'normal'

    myplot.Clf()
    myplot.Cdfs([cdf_p, cdf_n])
    myplot.Show()
    myplot.Close()


