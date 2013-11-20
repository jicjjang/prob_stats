import randvar
import thinkstats.thinkstats as ts
import math

def Sample():
    normal = randvar.Normal(0, 1)
    sample = [normal.generate() for x in range(6)]

    mean = ts.Mean(sample)
    dev2 = [(x - mean)**2 for x in sample]
    sn = sum(dev2) / float(len(dev2))
    sn_1 = sum(dev2) / float(len(dev2) - 1)
    
    return sn, sn_1

num_estimation = 10000
total_sn = 0
total_sn_1 = 0
for xx in range(num_estimation):
    sn, sn_1 = Sample()
    total_sn += (sn - 1)
    total_sn_1 += (sn_1 - 1)

print '# of estimation:', num_estimation

err = total_sn / float(num_estimation)
print "sample variance(Sn) expected error", err

err = total_sn_1 / float(num_estimation)
print "sample variance(Sn-1) expected error", err



    

    
