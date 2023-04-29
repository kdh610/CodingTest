
import sys
from heapq import *

INF=int(1e9)
v,e = map(int,input().split())
start = int(input())

graph=[[] for _ in range(v+1)]
distance=[INF]*(v+1)

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))



def dijstra(start):

    q = []

    heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, node = heappop(q)

        if dist > distance[node]:
            continue

        for i in graph[node]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heappush(q,(cost,i[0]))

dijstra(start)

for i in range(1,v+1):
    answer = distance[i]
    if answer==int(1e9):
        answer='INF'
    print(answer)