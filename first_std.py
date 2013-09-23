import thinkstats.thinkstats as ts
import thinkstats.first as first
import math

if __name__ == '__main__':
    data_dir = 'thinkstats'

    table, firsts, others = first.MakeTables(data_dir)
    first.ProcessTables(firsts, others)

    firsts.std = math.sqrt(ts.Var(firsts.lengths))
    others.std = math.sqrt(ts.Var(others.lengths))
        
    print 'Number of first babies', firsts.n
    print 'Number of others', others.n

    mu1, mu2 = firsts.mu, others.mu

    print 'Mean gestation in weeks:' 
    print 'First babies', mu1 
    print 'Others', mu2
    
    print 'Difference in days', (mu1 - mu2) * 7.0

    print ''
    print 'Standard Deviation:'
    print 'First babies', firsts.std
    print 'Others', others.std
    print 'Difference in days', (firsts.std - others.std) * 7.0
    
