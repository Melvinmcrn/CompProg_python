def det3(m):

    a = m[0][0]*m[1][1]*m[2][2]
    b = m[0][1]*m[1][2]*m[2][0]
    c = m[0][2]*m[1][0]*m[2][1]
    d = m[0][2]*m[1][1]*m[2][0]
    e = m[0][0]*m[1][2]*m[2][1]
    f = m[0][1]*m[1][0]*m[2][2]

    return a+b+c-d-e-f

#--------------------------------------------------------------------

def det4(m):

    a = m[0][0]
    b = m[0][1]
    c = m[0][2]
    d = m[0][3]

    e = m[1][0]
    f = m[1][1]
    g = m[1][2]
    h = m[1][3]
    
    i = m[2][0]
    j = m[2][1]
    k = m[2][2]
    l = m[2][3]

    M = m[3][0]
    n = m[3][1]
    o = m[3][2]
    p = m[3][3]

    return a*det3([[f,g,h], [j,k,l], [n,o,p]])-b*det3([[e,g,h], [i,k,l], [M,o,p]])+c*det3([[e,f,h], [i,j,l], [M,n,p]])-d*det3([[e,f,g], [i,j,k], [M,n,o]])

#main----------------------------------------------------------------

matrix = []
for i in range(4):
    matrix.append([int(e) for e in input().split()])

print(det4(matrix))
