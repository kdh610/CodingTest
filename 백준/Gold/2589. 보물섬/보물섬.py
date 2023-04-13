from collections import *
import copy

row, col = map(int,input().split())
MAP = [list(input()) for _ in range(row)]

land = []
for i in range(row):
    for j in range(col):
        if MAP[i][j]=='L':
            MAP[i][j] = 0
            land.append((i,j))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 0

def bfs(y,x):
    global answer
    temp = copy.deepcopy(MAP)
    temp[y][x] = 1
    Q = deque()
    Q.append((y,x))

    while Q:
        y,x = Q.popleft()

        for i in range(4):
            ny = y +dy[i]
            nx = x + dx[i]
            if 0<=ny<row and 0<=nx<col and temp[ny][nx]==0:
                temp[ny][nx] = temp[y][x] +1
                answer = max(answer,temp[ny][nx])
                Q.append((ny,nx))



for i,j in land:
        if MAP[i][j] == 0:

            bfs(i,j)

print(answer-1)