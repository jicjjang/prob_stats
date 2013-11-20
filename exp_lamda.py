import randvar
import thinkstats.thinkstats as ts
import math

p_lam = 1.0

def Sample():
    exp = randvar.Exponential(p_lam)
    sample = sorted([exp.generate() for x in range(6)])

    mean = ts.Mean(sample)
    median = ts.Mean(sample[2:4])

    return 1.0/mean, math.log(2)/median

num_estimation = 1000
total_sm = 0
total_med = 0
total_err = 0
total_err_m = 0
for xx in range(num_estimation):
    lam, lam_m = Sample()
    total_sm += (lam - p_lam)**2
    total_med += (lam_m - p_lam)**2
    total_err += (lam - p_lam)
    total_err_m += (lam_m - p_lam)

print '# of estimation:', num_estimation

MSE = total_sm / float(num_estimation)
print "lambda(using mean)'s MSE", MSE

MSE = total_med / float(num_estimation)
print "lambda(using median)'s MSE", MSE

err = total_err / float(num_estimation)
print "estimated lambda(using mean) expected error", err

err = total_err_m / float(num_estimation)
print "estimated lambda(using median) expected error", err



    

    
