import heapq
import sys
from heapq import *
v,e = map(int,input().split())

k = int(input())

graph = [[] for _ in range(v+1)]


for _ in range(e):
    a,b,c=map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

distance = [int(1e9)]*(v+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            node, c = i
            cost = dist + c

            if cost<distance[node]:
                distance[node]=cost
                heapq.heappush(q,(cost, node))
dijkstra(k)

# print(distance)

for i in range(1,v+1):
    if distance[i]==int(1e9):
        print('INF')
    else:
        print(distance[i])
