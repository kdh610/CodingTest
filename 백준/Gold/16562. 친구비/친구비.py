

import sys
from collections import *

n,m,k = map(int,input().split())
cost = list(map(int,sys.stdin.readline().split()))

parent=[ i for i in range(n+1)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    union(parent,a,b)



dict = defaultdict(int)

for i in range(1,len(parent)):
    a=find(parent, parent[i])
    if not dict[a]:
        dict[a] = cost[i - 1]
    else:
        dict[a] = min(dict[a], cost[i-1])


if k >= sum(dict.values()):
    print(sum(dict.values()))
else:
    print("Oh no")