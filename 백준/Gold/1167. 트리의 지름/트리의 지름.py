

from heapq import *
import sys

v = int(input())

graph = [ [] for _ in range(v+1)]


for _ in range(v):
    arr = list(map(int, sys.stdin.readline().split()))
    start, end, cost = 0,0,0
    for i, num in enumerate(arr):
        if num==-1:
            break
        if i==0:
            start = num
            continue
        if i%2==1:
            end = num
        else:
            graph[start].append((end, num))

def dijkstra(start):

    q = []
    distance = [int(1e9)] * (v+1)
    distance[start] = 0
    heappush(q,(0,start))
    MAX = 0
    idx = 0
    while q:
        dist, now = heappop(q)

        if distance[now] < dist: continue

        for node, cost in graph[now]:
            if distance[node]> dist+cost:
                distance[node] = dist+cost
                if MAX < dist+cost:
                    MAX = dist+cost
                    idx = node
                heappush(q,(dist+cost, node))

    return idx,MAX

idx,cost = dijkstra(1)
idx2, answer = dijkstra(idx)


print(answer)



