import sys
from collections import *

n=int(input())


arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
graph=defaultdict(list)
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            graph[i].append(j)



answer=[[0]*n for _ in range(n)]
for i in range(n):
    visit=[False]*(n)
    Q = deque()

    Q.append(i)


    while Q:
        node = Q.popleft()

        for k in graph[node]:
            if not visit[k]:
                answer[i][k]=1
                Q.append(k)
                visit[k]=True


for i in range(n):
    print(*answer[i],sep=' ')