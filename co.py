import thinkstats.correlation as co

print 'Covariance Test:'

xs = [1, 3, 5, 6, 7]
ys = [10, 30, 60, 70, 80]
zs = [7, 6, 5, 3, 1]
ns = [3, 2, 1, 2, 3]

print co.Cov(xs, ys)
print co.Cov(xs, zs)
print co.Cov(xs, ns)

print 'Correlation Test:'

print co.Corr(xs, ys)
print co.Corr(xs, zs)
print co.Corr(xs, ns)
