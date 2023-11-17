import sys
from collections import *

T = int(input())

dy=[0,0,1,-1]
dx=[1,-1,0,0]


for _ in range(T):
    m,n,k= map(int,sys.stdin.readline().split())

    field=[[0]*m for _ in range(n)]

    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        field[y][x]=1


    answer=0
    Q=deque()
    for i in range(n):
        for j in range(m):
            if field[i][j]==1:
                answer+=1
                Q.append((i,j))
                field[i][j]=-1

                while Q:
                    y,x=Q.popleft()

                    for k in range(4):
                        ny = y+dy[k]
                        nx = x+dx[k]

                        if 0<=ny<=n-1 and 0<=nx<=m-1:

                            if field[ny][nx]==1:
                                Q.append((ny,nx))
                                field[ny][nx]=-1
    print(answer)




