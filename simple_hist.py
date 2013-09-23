t = [1, 2, 3, 3, 5, 5, 5, 6, 6, 7]
hist = {}  # Dictionary
for x in t:
  hist[x] = hist.get(x, 0) + 1

n = float(len(t))
pmf = {}
for x, freq in hist.items():
  pmf[x] = freq / n


print 'Histogram:', hist
print 'PMF:', pmf
