import sys
from collections import *

n,m = map(int,sys.stdin.readline().split())

graph = defaultdict(list)

for i in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

Q = deque()
visit = [False]*(n+1)
cnt = 0

for i in range(1, n + 1):
    if visit[i] == False:
        visit[i]=True
        Q.append(i)
        cnt += 1
        while Q:
            node = Q.popleft()
            for j in graph[node]:
                if visit[j] == False:
                    visit[j]=True
                    Q.append(j)

print(cnt)