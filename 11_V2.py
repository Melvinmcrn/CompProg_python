import numpy as np

x = [float(e) for e in input().strip().split()]
rentalrates = np.array(x)
sales = np.zeros((4,5))

for k in range(4):

    sales[k,] = [int(e) for e in input().strip().split()]

totalsales = list(np.sum(sales,axis=0))

d = totalsales.index(np.max(totalsales))

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')

print(days[d],totalsales[d])
salesvalues = rentalrates.dot(sales)
out = ''
for c in salesvalues:
    out += str(c) + ' '

print(out.strip())

