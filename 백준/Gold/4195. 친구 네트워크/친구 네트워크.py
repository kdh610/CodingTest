from collections import *
import sys

t = int(input())

def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a=find(parent,a)
    b = find(parent, b)
    if a==b:
        return
    if a<b:
        parent[b]=a
        number[a]+=number[b]
    else:
        parent[a] = b
        number[b] += number[a]

for i in range(t):
    parent = defaultdict()
    number = defaultdict()
    n = int(input())
    for j in range(n):
        a, b = map(str, sys.stdin.readline().split())
        if a not in parent.keys():
            parent[a]=a
            number[a]=1
        if b not in parent.keys():
            parent[b] = b
            number[b]=1

        union(parent,a,b)

        parent_tmp = find(parent,a)
        print(number[parent_tmp])


