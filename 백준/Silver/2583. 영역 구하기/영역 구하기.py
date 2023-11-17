import sys
from collections import *

m,n,k = map(int,input().split())

field=[[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

    for i in range(y1, y2):
        for j in range(x1,x2):
            field[i][j]=1


dy=[0,0,1,-1]
dx=[1,-1,0,0]
Q=deque()

result=[]
for i in range(m):
    for j in range(n):
        if field[i][j]==0:

            cnt=1
            Q.append((i,j))
            field[i][j]=-1

            while Q:
                y,x=Q.popleft()

                for k in range(4):
                    ny=y+dy[k]
                    nx=x+dx[k]

                    if 0<=ny<m and 0<=nx<n and field[ny][nx]==0:
                        cnt+=1
                        Q.append((ny,nx))
                        field[ny][nx]=-1

            result.append(cnt)

result.sort()
print(len(result))
print(*result)






