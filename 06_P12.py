s=input().strip()
queue=[]

for i in range(len(s)):
    queue.append(s[i])

n=int(input())

for i in range(n):

    order=input().strip().split()

    if order[0]=='in':
        queue.insert(int(order[2]),order[1])
        
    elif order[0]=='out':
        queue.pop(int(order[1]))

    elif order[0]=='swap':
        queue[int(order[1])],queue[int(order[2])]=queue[int(order[2])],queue[int(order[1])]

    out=''
    print(out.join(queue))
