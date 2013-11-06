import randvar
from thinkstats import Cdf
from thinkstats import myplot
from thinkstats import thinkstats
from thinkstats import rankit
import math

def ex6_12(n, ns=1000):
    exp = randvar.Exponential(1)
    
    s = [sum([exp.generate() for x in range(n)])/float(n) for i in range(ns)]

    mu, var = thinkstats.MeanVar(s)
    print n, mu, var

    cdf = Cdf.MakeCdfFromList(s)
    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save('clt'+str(n))
    myplot.Close()

def ex6_13(n, ns=1000):
    exp = randvar.Exponential(1)
    
    s = [sum([exp.generate() for x in range(n)]) for i in range(ns)]

    mu, var = thinkstats.MeanVar(s)
    print n, mu, var

    cdf = Cdf.MakeCdfFromList(s)
    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save('clt13'+str(n))

    rankit.MakeNormalPlot(s, 'clt13npp'+str(n))

    myplot.Close()

def ex6_14(n, ns=1000):
    exp = randvar.Exponential(1)

    def prod_log(t):
        p = 1
        for x in t:
            p = p * x
        return math.log(p)
    
    s = [prod_log([exp.generate() for x in range(n)]) for i in range(ns)]

    mu, var = thinkstats.MeanVar(s)
    print n, mu, var

    cdf = Cdf.MakeCdfFromList(s)
    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save('clt14'+str(n))

    rankit.MakeNormalPlot(s, 'clt14npp'+str(n))

    myplot.Close()

if __name__=='__main__':
    ex6_12(5)
    ex6_12(10)
    ex6_12(100)

    ex6_13(2)
    ex6_13(4)
    ex6_13(8)

    ex6_14(2)
    ex6_14(4)
    ex6_14(8)
