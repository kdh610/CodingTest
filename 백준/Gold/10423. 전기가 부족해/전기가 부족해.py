
import sys

n,m,k = map(int,input().split())

power = list(map(int,input().split()))

cables = [ list(map(int,sys.stdin.readline().split())) for _ in range(m)]


cables.sort(key=lambda x:x[2])

parent = [i for i in range(n+1)]

for i in range(len(parent)):
    if i in power:
        parent[i]=-1


def find(parent, x):
    if parent[x]==-1:
        return -1

    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]


def union(a,b):
    a = find(parent, a)
    b = find(parent, b)
    # print('a',a)
    # print('b',b)
    if a==b:
        return False

    if a>b:
        parent[a]=b
    else:
        parent[b]=a
    return True


cost=0

for cable in cables:
    a,b,c = cable
    # print(a,b,c)
    if not union(a,b):
        continue
    cost+=c
    # print(parent)
    if sum(parent)==-(n):
        break
# print(parent)

print(cost)











