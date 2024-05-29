

from collections import *
from heapq import *
import sys
t = int(input())


for _ in range(t):

    n,d,c = map(int,input().split())

    graph = defaultdict(list)
    distance = [int(1e9)] * (n+1)
    distance[c] = 0

    for _ in range(d):
        a,b,s = map(int,sys.stdin.readline().split())
        graph[b].append((a,s))

    q = []
    heappush(q,(0,c))

    while q:
        dist, cur = heappop(q)
        if distance[cur] < dist: continue

        for i in graph[cur]:
            node, cost = i
            if distance[node]>dist+cost:
                distance[node] = dist+cost
                heappush(q,(distance[node], node))

    cnt = 0
    time = 0

    for i in range(1,(n+1)):
        if distance[i]!=int(1e9):
            cnt+=1
            time = max(time, distance[i])

    print(cnt,time)