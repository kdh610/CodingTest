import sys
from collections import *

T=int(input())

for _ in range(T):
    n=int(sys.stdin.readline().strip())
    students=[0]+list(map(int,sys.stdin.readline().split()))

    team=0
    visit = [False] * (n + 1)
    for i in range(1,n+1):
        cycle=[]
        if not visit[i]:
            Q=deque()
            Q.append(i)
            visit[i]=True
            cycle.append(i)

            while Q:
                j = Q.popleft()

                if not visit[students[j]]:
                    visit[students[j]]=True
                    Q.append(students[j])
                    cycle.append(students[j])
                else:
                    if students[j] in cycle:
                        team+=len(cycle[cycle.index(students[j]):])

    print(n-team)



