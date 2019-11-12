import math
R=float(input())
G=float(input())
B=float(input())
H=2*math.pi-math.acos(((R-G)+(R-B))/(2*math.sqrt((R-G)**2+(R-B)*(G-B))))
S=1-(3*R/(R+G+B))
I=(R+G+B)/3
print(H)
print(S)
print(I)
