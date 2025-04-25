import sys
from collections import *
sys.setrecursionlimit(10**6)
v,e = map(int,input().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(e)]



parent = [i for i in range(v+1)]


def find(x, parent):

    if parent[x]!=x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a,b):
    a = find(a,parent)
    b = find(b,parent)

    if a==b:
        return False

    parent[b]=a
    return True


graph.sort(key=lambda x: x[2])

answer = 0
cnt = 0
for i in graph:
    a,b,c = i

    if not union(a,b):
        continue
    cnt+=1
    answer+=c
    
    if cnt==v-1:
        break

print(answer)
