
import sys
from collections import *

p,w = map(int,sys.stdin.readline().split())
c,v = map(int,sys.stdin.readline().split())

edge=[]

for i in range(w):
    a,b,cost = map(int,sys.stdin.readline().split())
    edge.append((cost,a,b))


edge.sort(reverse=True)

def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a=find(parent,a)
    b= find(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

parent=[i for i in range(p+1)]

for node in edge:
    cost,a,b = node

    union(parent, a, b)
    if find(parent,c) == find(parent,v):
        answer=cost
        break


print(answer)