import numpy as np

n = int(input())

scores = np.ones((n-3,6),float)
for i in range(n):

    x = input().strip().split(',')
        
    if i >= 3:

        scores[i-3,] = [float(e) for e in x[1:]]

scores = np.sum(scores,axis = 1)

for c in scores:
    print(c)
