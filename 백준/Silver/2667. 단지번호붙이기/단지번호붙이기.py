import sys
from collections import *

n=int(input())

map=[list(sys.stdin.readline().strip()) for _ in range(n)]

dy=[0,0,1,-1]
dx=[1,-1,0,0]
Q=deque()
danji=0
result=[]
for i in range(n):
    for j in range(n):
        if map[i][j]=='1':
            danji+=1
            cnt=1
            Q.append((i,j))
            map[i][j]=-1

            while Q:
                y,x=Q.popleft()

                for k in range(4):

                    ny=y+dy[k]
                    nx=x+dx[k]
                    if 0<=ny<n and 0<=nx<n and map[ny][nx]=='1':
                        Q.append((ny,nx))
                        map[ny][nx]=-1
                        cnt+=1
            result.append(cnt)

result.sort()
print(danji)
print(*result,sep='\n')






