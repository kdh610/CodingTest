import sys
input = sys.stdin.readline

while True:
    m,n = map(int,input().split())

    if m==0 and n==0:
        break


    street = [list(map(int,input().split())) for _ in range(n)]

    total = 0
    for a,b,c in street:
        total+=c

    street.sort(key=lambda x:x[2])

    parent = [i for i in range(m)]

    def find(parent,x):
        if parent[x]!=x:
            parent[x] = find(parent,parent[x])
        return parent[x]

    def union(a,b):
        a= find(parent,a)
        b = find(parent, b)
        if a==b: return False
        parent[b] =a
        return True

    cnt=0
    cost =0
    for a,b,c in street:
        if not union(a,b): continue
        cost+=c
        cnt+=1
        if cnt==m-1:
            break

    print(total-cost)