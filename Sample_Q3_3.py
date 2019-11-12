n = int(input())

data_like = dict()
data_liked = dict()
for i in range(n):

    x = input().strip().split()

    if x[0] not in data_like:
        data_like[x[0]] = set(x[1:])

    else:
        data_like[x[0]] = data_like[x[0]].union(set(x[1:]))

    for c in x[1:]:
        if c not in data_liked:
            data_liked[c] = set(x[0:1])

        else:
            data_liked[c] = data_liked[c].union(set(x[0:1]))

while True:

    order = input().strip().split()

    if order[0] == 'exit':
        break

    elif order[0] == 'common' and order[1] == 'page':

        if order[2] not in data_like:
            common = set()
        else:
            common = data_like[order[2]]
        
        for c in order[2:]:

            if c not in data_like:
                common = common & set()
            else:
                common = common & data_like[c]

        print(len(common))
            
    elif order[0] == 'common' and order[1] == 'user':

        if order[2] not in data_liked:
            common = set()
        else:
            common = data_liked[order[2]]

        for c in order[2:]:

            if c not in data_liked:
                common = common & set()
            else:
                common = common & data_liked[c]

        print(len(common))

    elif order[0] == 'similar' and order[1] == 'user':

        if order[2] not in data_like:
            person_like = set()
        else:
            person_like = data_like[order[2]]

        common = []

        most = [0,0]
        for i,c in data_like.items():
            if i != order[2]:
    
                same = len(person_like & c) / len(person_like | c)
                common.append([i,same])
                if same > most[1]:
                    most = [common.index([i,same]),same]
                elif same == most[1] and i < common[most[0]][0]:
                    most = [common.index([i,same]),same]
                    

        print(common[most[0]][0])

    elif order[0] == 'similar' and order[1] == 'page':
        
        
        if order[2] not in data_liked:
            page_like = set()
        else:
            page_like = data_liked[order[2]]

        common = []

        most = [0,0]
        for i,c in data_liked.items():
            if i != order[2]:
    
                same = len(page_like & c) / len(page_like | c)
                common.append([i,same])
                if same > most[1]:
                    most = [common.index([i,same]),same]
                elif same == most[1] and i < common[most[0]][0]:
                    most = [common.index([i,same]),same]
                    

        print(common[most[0]][0])
