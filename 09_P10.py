def distance(p, q):

    return  ( (p[0]-q[0])**2 + (p[1]-q[1])**2 )**0.5 

#----------------------------------------------------------------

def perimeter(points):

    sum=distance(points[0],points[-1])
    for i in range(len(points)-1):
        sum+=distance(points[i],points[i+1])

    return sum

#main------------------------------------------------------------

s = input().strip().split()
p = [(float(t[1:t.find(',')]),float(t[t.find(',')+1:-1])) for t in s]
print(perimeter(p))
