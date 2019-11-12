def read_data():
    D = dict()
    n = int(input())
    for k in range(n):
        sid,name,gpax,year,dept = [e.strip() for e in input().strip().split(',')]
        gpax = float(gpax); year = int(year)
        if dept not in D :
            D[dept] = {sid:(name,gpax,year)}
        else :
            D[dept][sid] = (name,gpax,year)

    return D

#-------------------------------------------------------------------- 
def is_in(D, sid, dept):

    if dept in D:
        if sid in D[dept].keys():
            return True

    return False

#--------------------------------------------------------------------
def get_year(D, sid):

    for i,c in D.items():
        if sid in c:
            return D[i][sid][2]
        
    return False

#--------------------------------------------------------------------
def get_supers(D, dept):

    out = set()
    if dept not in D:
        return False

    for i,v in D[dept].items():

        if v[2] > 4:
            out.add(i)

    return out

#--------------------------------------------------------------------
def max_gpax(D):

    out = 0
    for i,v in D.items():
        for c in v.values():
            if c[1] > out:
                out = c[1]

    return out

#--------------------------------------------------------------------
def get_max_gpax_students(D):

    gpax = max_gpax(D)
    out = set()

    for i,v in D.items():
        for j,c in v.items():
            if c[1] == gpax:
                out.add((j,c[0]))
    
    return out

#main================================================================
    
# do not remove the following lines!!
n = int(input())
for k in range(n):
    exec(input().strip()) 
