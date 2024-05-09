from collections import *
def solution(n, k, cmd):
    answer = ['O']*n
    stack = []


    link = defaultdict()
    link[-1] = [-2,0]
    link[0] = [-1,1]
    link[n-1] = [n-2,n]
    link[n] = [n-1,n+1]
    for i in range(1,n):
        link[i] = [i-1,i+1]


    cur = k
    prev = k-1
    next = k+1

    for c in cmd:
        if len(c)>1:
            command, num = c.split(' ')
        else:
            command = c

        prev = link[cur][0]
        next = link[cur][1]

        if command=='C':
            link[prev][1] = link[cur][1]
            link[next][0] = link[cur][0]
            answer[cur]='X'
            stack.append(cur)
            if next==n:
                cur = link[cur][0]
            else:
                cur = link[cur][1]
        elif command=='Z':
            pop = stack.pop()
            prev = link[pop][0]
            next = link[pop][1]

            link[pop][1] = link[prev][1]
            link[prev][1] = pop
            link[pop][0] = link[next][0]
            link[next][0] = pop
            answer[pop]="O"
        else:
            dir = -1
            if command == 'U':
                # cur -= int(num)
                dir=0
            elif command == 'D':
                # cur += int(num)
                dir=1
            for i in range(int(num)):
                cur = link[cur][dir]

    return "".join(answer)