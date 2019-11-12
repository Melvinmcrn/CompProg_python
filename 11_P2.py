import numpy as np

n = int(input())

price = np.ndarray((n,1))
for i in range(n):

    x = input().strip().split('\t')
    price[i,] = x[1:]

sales = np.ndarray((n,5))
for i in range(n):

    x = input().strip().split('\t')
    sales[i,] = x[1:]

price_total = sum(price*sales)

for c in price_total:
    print(c)
