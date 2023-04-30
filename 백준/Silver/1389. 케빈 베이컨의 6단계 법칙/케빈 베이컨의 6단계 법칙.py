import sys
from collections import *

n,m = map(int,sys.stdin.readline().split())
friend = defaultdict(list)
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)

def bfs(person):
    Q = deque()
    Q.append(person)
    visit = [0]*(n+1)
    while Q:
        p = Q.popleft()

        for i in friend[p]:
            if i == person:
                continue
            if visit[i] == 0:
                visit[i] = visit[p] + 1
                Q.append(i)
    return sum(visit)

result = []
MIN = 10000000
for i in range(1,n+1):
    x = bfs(i)
    if MIN > x:
        MIN = x
        result = i

print(result)





