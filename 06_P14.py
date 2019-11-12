book=[]

while True:

    order=input().strip()

    if order[:3]=='end':
        break

    elif order[:6]=='return':
        book.append(order[7:])
        print(len(book))

    elif order[:5]=='shelf':
        if len(book)==0:
            print('no book')

        else:
            print(book[-1])
            book.pop(-1)

    elif order[:3]=='top':
        if len(book)==0:
            print('no book')

        else:
            print(book[-1])

    elif order[:4]=='list':
        print(book)
