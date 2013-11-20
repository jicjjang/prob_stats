import randvar
import thinkstats.thinkstats as ts
import math

def Sample():
    normal = randvar.Normal(0, 1)
    sample = sorted([normal.generate() for x in range(6)])
    
    return ts.Mean(sample), ts.Mean(sample[2:4])

total_sm = 0
total_med = 0
for xx in range(1000):
    mean, median = Sample()
    total_sm += (mean - 0) * (mean - 0)
    total_med += (median - 0) * (median - 0)

MSE = total_sm / 1000.0
print "sample mean's MSE", MSE

MSE = total_med / 1000.0
print "sample median's MSE", MSE



    

    
