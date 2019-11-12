def compare(a, b):

    if a[1]<b[1]:
        return True
    elif a[1]==b[1] and a[0]>b[0]:
        return True

    return False

#main-----------------------------------------------------------

n = int(input().strip())
d = []

for i in range(n):
    x, y = input().strip().split()
    d.append((x, float(y)))

for k in range(n-1):
    for i in range(n-1):
        if compare(d[i],d[i+1]):
            d[i], d[i+1] = d[i+1], d[i]

for i in d:
    print(i[0], i[1])
