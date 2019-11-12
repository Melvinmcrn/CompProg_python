num = int(input())

q = []
i = 0
time = dict()
wait_time = 0
customer_count = 0
for z in range(num):

    order = input().strip().split()

    if order[0] == 'reset':
        n = int(order[1])

    elif order[0] == 'new':
        print('ticket',n)
        q.append(n)
        time[n] = int(order[1])
        n += 1

    elif order[0] == 'next':
        print('call',q[i])
        i += 1

    elif order[0] == 'order':
        dt = (int(order[1]) - time[q[i-1]])
        print('qtime',q[i-1],dt)
        wait_time += dt
        customer_count += 1

    elif order[0] == 'avg_qtime':
        avg = wait_time / customer_count
        print('avg_qtime',round(avg,4))
