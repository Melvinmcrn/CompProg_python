def knows(R,x,y):

    if y in R[x]:
        return True
    else:
        return False

#-------------------------------------------------------------------

def is_celeb(R,x):
    
    if len(R[x])>0 and x not in R[x]:
        return False
    
    for c in R.keys():            
            
          if (not knows(R,c,x)) and c!=x:
              return False
    else:
        return True

#-------------------------------------------------------------------

def find_celeb(R):

    for x in R:
        if is_celeb(R,x):
            return x
    else:
        return None

#-------------------------------------------------------------------

def read_relations():

    R=dict()
    while True:

        d=input().strip()

        if len(d) == 1: break

        d=d.split()

        if d[0] in R:
            R[d[0]].add(d[1])
        elif d[0] not in R:
            R[d[0]]=set()
            R[d[0]].add(d[1])

        if d[1] not in R:
            R[d[1]]=set()

    return R

        

#-------------------------------------------------------------------

def main():
    R=read_relations()
    c=find_celeb(R)
    if c==None:
        print('Not Found')
    else:
        print(c)

#main---------------------------------------------------------------
        
exec(input().strip())
