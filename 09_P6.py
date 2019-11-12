def read_data():

    docs = {}
    n = int(input().strip())

    for i in range(n):

        tokens = input().strip().split()
        doc_name = tokens[0]
        doc_keywords = tokens[1:]

        for kword in doc_keywords:
            if kword in docs.keys():
                docs[kword].add(doc_name)
            else:
                docs[kword] = {doc_name}

    return docs

#---------------------------------------------------------------

def search(docs, condition, search_keywords):

    if condition=='or':
        out=set()
        for m in search_keywords:
            if m in docs:
                for c in docs[m]:
                    out.add(c)

        return list(out)

    elif condition=='and':
        out=set()
        check=True
        for c in search_keywords:
            if c not in docs:
                return []
            
            if check:
                out.update(docs[c])
                check=False
            else:
#                print('out=',out,'\nc=',c,'\ndocs[c]=',docs[c])
                out=out&docs[c]
#                print('out2=',out)

        return list(out)

    else:
        return []

#====  Program starts here =======================

docs = read_data()
tokens = input().split()
print( sorted( search(docs, tokens[0], tokens[1:]) ) )

#=================================================
