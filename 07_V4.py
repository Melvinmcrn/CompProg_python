e=input().strip()
this_year,this_month,this_day=int(e[:4]),int(e[4:6]),int(e[6:])

file=open('circulations.txt')

book_list=[]
year,month,day=[],[],[]

#make a list of book
for line in file:

    book,member,due=line.strip().split()
    book_list.append([book,member,due,int(due[:4]),int(due[4:6]),int(due[6:])])

file.close()

#make an overdue book list
overdue_book=[]
for c in book_list:

    if c[3]<this_year:
        overdue_book.append(c)

    elif c[3]==this_year:

        if c[4]<this_month:
            overdue_book.append(c)

        elif c[4]==this_month:

            if c[5]<this_day:
                overdue_book.append(c)
                        
#make an output list
out_book=[]
for c in overdue_book:

    check=True
    for d in out_book:

        if d[3]>c[3]:
            out_book.insert(out_book.index(d),c)
            check=False
            break

        elif d[3]==c[3]:

            if d[4]>c[4]:
                out_book.insert(out_book.index(d),c)
                check=False
                break

            elif d[4]==c[4]:

                if d[5]>c[5]:
                    out_book.insert(out_book.index(d),c)
                    check=False
                    break

    if check:
        out_book.append(c)

        
#print out
for c in out_book:
    
    print(c[0],c[1],c[2])

if len(out_book)==0:
    print('Not Found')
