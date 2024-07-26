

n, m = map(int,input().split())


up = [ [int(1e9)]*(n+1) for _ in range(n+1) ]
down = [ [int(1e9)]*(n+1) for _ in range(n+1) ]

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            up[i][j]=0
            down[i][j]=0

for i in range(m):
    a,b = map(int,input().split())
    up[b][a]=1
    down[a][b]=1

answer = 0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            up[a][b] = min( up[a][b], up[a][k] + up[k][b])
            down[a][b] = min(down[a][b], down[a][k] + down[k][b])

# print(*up, sep='\n')
# print()
# print(*down, sep='\n')



for i in range(1,n+1):
    up_cnt=0
    down_cnt=0
    for j in range(1,n+1):
        if 0<up[i][j]<int(1e9):
            up_cnt+=1
        if 0<down[i][j]<int(1e9):
            down_cnt+=1

    if up_cnt>= (n+1)//2:
        answer+=1
    if down_cnt>= (n+1)//2:
        answer+=1

print(answer)




