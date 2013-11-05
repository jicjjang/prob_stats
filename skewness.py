from thinkstats import first
from thinkstats import descriptive
import math
from thinkstats import Cdf
from thinkstats import Pmf
from thinkstats import survey
from thinkstats import thinkstats

import matplotlib.pyplot as pyplot
from thinkstats import myplot


def Process(table, name):
    descriptive.Process(table, name)

    table.weights = [p.totalwgt_oz for p in table.records
                     if p.totalwgt_oz != 'NA']
    table.weight_pmf = Pmf.MakePmfFromList(table.weights, table.name)
    table.weight_cdf = Cdf.MakeCdfFromList(table.weights, table.name)

    table.lengths_pmf = Pmf.MakePmfFromList(table.lengths, table.name)
    table.legnths_cdf = Cdf.MakeCdfFromList(table.lengths, table.name)


def MakeTables(data_dir='.'):
    """Reads survey data and returns a tuple of Tables"""
    table, firsts, others = first.MakeTables(data_dir)
    pool = descriptive.PoolRecords(firsts, others)

    Process(pool, 'live births')
        
    return pool



def MakeFigures(pool):
    myplot.Clf()
    myplot.Hist(pool.weight_pmf, linewidth=1, color='blue')
    myplot.Save(root='nsfg_birthwgt_pmf',
                title='Birth weight PMF',
                xlabel='weight (ounces)',
                ylabel='probability')

    myplot.Clf()
    myplot.Cdf(pool.lengths_pmf, linewidth=1, color='blue')
    myplot.Save(root='nsfg_weeks_pmf',
                title='Gestation PMF',
                xlabel='weeks',
                ylabel='probability')

def Var3(t, mu=None):
    if mu is None:
        mu = thinkstats.Mean(t)

    # compute the squared deviations and return their mean.
    dev2 = [(x - mu)**3 for x in t]
    var = thinkstats.Mean(dev2)
    return var

def Skewness(t):
    return Var3(t)/math.pow(thinkstats.Var(t), 3/2.0)

def Median(t):
    st = sorted(t)
    mid = len(t) / 2
    if len(t) % 2 == 0:
        return (st[mid-1] + st[mid])/2.0
    else:
        return st[mid]

def PearsonSkewness(t):
    return 3.0 * (thinkstats.Mean(t) - Median(t)) / math.sqrt(thinkstats.Var(t))

def main(name, data_dir='thinkstats'):

    pool = MakeTables(data_dir)

    print 'Skewness of weights:', Skewness(pool.weights)
    print 'Skewness of gestations:', Skewness(pool.lengths)
    
    print "Pearson's Skewness of weights:", PearsonSkewness(pool.weights)
    print "Pearson's Skewness of gestations:", PearsonSkewness(pool.lengths)
    
    MakeFigures(pool)

    myplot.Close()

if __name__ == '__main__':
    import sys
    main(*sys.argv)
