import collections
import sys
from collections import *


n,m,v = map(int, input().split())

graph = collections.defaultdict(list)
queue = deque()
result = []

for i in range(m):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph.keys():
    graph[i].sort()

def dfs(v, result):
    result.append(v)
    for i in graph[v]:
        if i not in result:
            result = dfs(i, result)
    return result


def bfs(v):
    queue.append(v)
    result.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i in result:
                continue
            else:
                queue.append(i)
                result.append(i)
    return result


dfs(v,result)
print(*result)
result.clear()
bfs(v)
print(*result)