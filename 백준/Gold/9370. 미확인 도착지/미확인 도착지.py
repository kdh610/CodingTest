
import sys
import heapq
from collections import *
import copy

def dijkstra(start, distance, graph):

    distance[start] = 0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        # print('now',now)

        if dist>distance[now]:
            continue

        for node,c in graph[now]:
            # print(c,node)
            cost = dist + c
            if cost < distance[node]:
                distance[node] = cost
                q.append((cost, node))

    return distance


T = int(input())

for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    graph = [ [] for _ in range(n+1)]

    for _ in range(m):
        a,b,d = map(int,sys.stdin.readline().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    target = [int(sys.stdin.readline()) for _ in range(t)]


    Ds = dijkstra(s, [int(1e9)] * (n + 1), graph)
    Dg = dijkstra(g, [int(1e9)] * (n + 1), graph)
    Dh = dijkstra(h, [int(1e9)] * (n + 1), graph)

    answer = []
    for end in target:
        if Ds[end]==int(1e9):
            continue

        if Ds[g]+Dg[h]+Dh[end] == Ds[end] or Ds[h]+Dh[g]+Dg[end]==Ds[end]:
            answer.append(end)
    answer.sort()
    print(*answer)















