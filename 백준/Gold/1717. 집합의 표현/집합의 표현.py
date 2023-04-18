import sys
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent,a,b):
    a = find(parent,a)
    b = find(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    type, a, b = map(int,sys.stdin.readline().split())

    if type == 0:
        union(parent,a,b)
    elif type ==1:
        a=find(parent,a)
        b=find(parent,b)
        if a==b:
            print("YES")
        else:
            print("NO")

