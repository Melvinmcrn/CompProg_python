x=[int(e) for e in input().split()]

for k in range(len(x)-1):

    minIdx = k
    minVal = x[k]

    for i in range(k,len(x)):

        if x[i] < minVal:

            minIdx = i
            minVal = x[i]

    x[k],x[minIdx] = x[minIdx],x[k]

print(x)
