heights = [int(e) for e in input().strip().split()]
h = int(input())
heights.sort()

if h<heights[0]:
    print('Too short')
elif h>heights[-1]:
    print('Too tall')

else:

    i = 0
    p = 100.0

    while i < len(heights):

        if heights[i] > h:
            p = i*100/len(heights)
            break
        else:
            i+=1

    print(str(p) + 'th percentile')
