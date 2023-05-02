import sys
from heapq import *

INF=int(1e9)

n, m, x = map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]



for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())

    graph[a].append((b,c))


def dijkstra(start):
    distance = [INF] * (n + 1)
    q=[]
    heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now = heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]]=cost
                heappush(q,(cost,i[0]))
    return distance

answer = 0
arrival = dijkstra(x)
for i in range(1,n+1):
    depart = dijkstra(i)

    answer=max(answer,depart[x]+arrival[i])


print(answer)


