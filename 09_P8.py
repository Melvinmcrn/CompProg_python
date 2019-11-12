def isSet(c1,c2,c3):

    if c1[0]==c2[0] and c2[0]==c3[0]:
        None
    elif c1[0]!=c2[0] and c2[0]!=c3[0] and c1[0]!=c3[0]:
        None
    else:
        return False

    if c1[1]==c2[1] and c2[1]==c3[1]:
        None
    elif c1[1]!=c2[1] and c2[1]!=c3[1] and c1[1]!=c3[1]:
        None
    else:
        return False

    if c1[2]==c2[2] and c2[2]==c3[2]:
        None
    elif c1[2]!=c2[2] and c2[2]!=c3[2] and c1[2]!=c3[2]:
        None
    else:
        return False

    if c1[3]==c2[3] and c2[3]==c3[3]:
        None
    elif c1[3]!=c2[3] and c2[3]!=c3[3] and c1[3]!=c3[3]:
        None
    else:
        return False
    
    return True

#main---------------------------------------------------------

cards=[]
for i in range(12):
    cards.append(input().strip().split())

for i in range(12):
    for j in range(i+1,12):
        for k in range(j+1,12):
            if isSet(cards[i],cards[j],cards[k]):
                print(i,j,k)
