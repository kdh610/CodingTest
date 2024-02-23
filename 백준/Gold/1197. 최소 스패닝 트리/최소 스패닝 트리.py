import sys

V,E = map(int,input().split())

edge = [list(map(int,sys.stdin.readline().split())) for _ in range(E)]

parent=[0]*(V+1)

for i in range(1,V+1):
    parent[i] = i

edge.sort(key=lambda x:x[2])

def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(a,b):
    a=find(parent,a)
    b=find(parent,b)

    if a==b : return False

    parent[b] = a
    return True

weight=0
cnt=0
for i in edge:
    a,b,c = i
    if not union(a,b): continue
    weight+=c
    cnt+=1
    if cnt==V-1:
        break

print(weight)
